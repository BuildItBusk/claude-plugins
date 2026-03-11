"""Gather dynamic PR context: source branch, commits, and diff stat.

Outputs a compact summary for skill injection via !`python ...`.
"""

import json
import subprocess
import sys


def run(cmd: str) -> str:
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def main() -> None:
    default_ref = run("git symbolic-ref refs/remotes/origin/HEAD")
    default_branch = default_ref.removeprefix("refs/remotes/origin/") if default_ref else "main"

    source_branch = run("git branch --show-current")
    if not source_branch or source_branch == default_branch:
        print(f"ERROR: On '{source_branch or '(detached)'}' — switch to a feature branch first.", file=sys.stderr)
        sys.exit(1)

    log = run(f"git log origin/{default_branch}..HEAD --format=%s --max-count=10")
    diff_stat = run(f"git diff origin/{default_branch}...HEAD --stat --stat-width=60")

    ctx = {
        "source_branch": source_branch,
        "default_branch": default_branch,
        "commits": log.splitlines() if log else [],
        "diff_stat": diff_stat,
    }
    print(json.dumps(ctx))


if __name__ == "__main__":
    main()
