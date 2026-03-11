"""Attempt to detect Azure DevOps org, project, and repo from git remote.

Outputs JSON with detected values, or empty strings for what couldn't be parsed.
"""

import json
import re
import subprocess
import sys


def run(cmd: str) -> str:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def parse_ado_remote(url: str) -> dict:
    """Extract org, project, and repo from an Azure DevOps remote URL."""
    # SSH: git@ssh.dev.azure.com:v3/org/project/repo
    m = re.match(r"git@ssh\.dev\.azure\.com:v3/([^/]+)/([^/]+)/([^/]+)", url)
    if m:
        return {"org": m.group(1), "project": m.group(2), "repository": m.group(3)}
    # HTTPS: https://dev.azure.com/org/project/_git/repo
    m = re.match(r"https://dev\.azure\.com/([^/]+)/([^/]+)/_git/([^/]+)", url)
    if m:
        return {"org": m.group(1), "project": m.group(2), "repository": m.group(3)}
    # Legacy: https://org.visualstudio.com/project/_git/repo
    m = re.match(r"https://([^.]+)\.visualstudio\.com/([^/]+)/_git/([^/]+)", url)
    if m:
        return {"org": m.group(1), "project": m.group(2), "repository": m.group(3)}
    return {"org": "", "project": "", "repository": ""}


def main() -> None:
    remote_url = run("git remote get-url origin")
    if not remote_url:
        print(json.dumps({"org": "", "project": "", "repository": "", "remote": ""}))
        sys.exit(0)

    result = parse_ado_remote(remote_url)
    result["remote"] = remote_url

    default_ref = run("git symbolic-ref refs/remotes/origin/HEAD")
    result["default_branch"] = default_ref.removeprefix("refs/remotes/origin/") if default_ref else "main"

    print(json.dumps(result))


if __name__ == "__main__":
    main()
