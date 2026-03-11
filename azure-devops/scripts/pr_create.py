"""Create an Azure DevOps pull request.

Usage: python pr_create.py <title> <description> [target-branch]

Reads org/project/repo from .azure-devops.json in the repo root.
Pushes the current branch if needed, then creates the PR.
"""

import json
import subprocess
import sys
from pathlib import Path


def run(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, check=check)


def find_config() -> dict:
    """Walk up from cwd to find .azure-devops.json."""
    path = Path.cwd()
    while path != path.parent:
        config_file = path / ".azure-devops.json"
        if config_file.exists():
            return json.loads(config_file.read_text())
        path = path.parent
    print("ERROR: No .azure-devops.json found. Create one in the repo root with org, project, and repository.", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if len(sys.argv) < 3:
        print("Usage: python pr_create.py <title> <description> [target-branch]", file=sys.stderr)
        sys.exit(1)

    title = sys.argv[1]
    description = sys.argv[2]
    config = find_config()

    org = config.get("org")
    project = config.get("project")
    repo = config.get("repository")
    if not all([org, project, repo]):
        print("ERROR: .azure-devops.json must contain org, project, and repository.", file=sys.stderr)
        sys.exit(1)

    source = run("git branch --show-current").stdout.strip()
    target = sys.argv[3] if len(sys.argv) > 3 else config.get("default_branch", "main")

    # Push branch if no upstream
    tracking = run(f"git rev-parse --abbrev-ref {source}@{{upstream}}", check=False)
    if tracking.returncode != 0:
        print(f"Pushing {source} to origin...")
        run(f"git push -u origin {source}")

    org_url = f"https://dev.azure.com/{org}" if not org.startswith("https://") else org

    result = run(
        f'az repos pr create'
        f' --org "{org_url}"'
        f' --project "{project}"'
        f' --repository "{repo}"'
        f' --source-branch "{source}"'
        f' --target-branch "{target}"'
        f' --title "{title}"'
        f' --description "{description}"'
        f' --open',
        check=False,
    )

    if result.returncode != 0:
        print(f"ERROR: {result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)

    pr = json.loads(result.stdout)
    pr_id = pr.get("pullRequestId", "?")
    pr_url = f"{org_url}/{project}/_git/{repo}/pullrequest/{pr_id}"
    print(pr_url)


if __name__ == "__main__":
    main()
