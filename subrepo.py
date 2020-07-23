import os
import sys
from shutil import which
from subprocess import call

CURRENT_DIR = os.path.dirname(__file__)
GIT_SUBREPO_ROOT = os.path.join(CURRENT_DIR, "subrepo")


def main() -> int:
    git = which("git")
    if git is None:
        print("git executable was not found in PATH", file=sys.stderr)
        return 1

    env = dict(os.environ)
    path = os.getenv("PATH", "")
    env["GIT_SUBREPO_ROOT"] = GIT_SUBREPO_ROOT
    env["PATH"] = os.pathsep.join((path, os.path.join(GIT_SUBREPO_ROOT, "lib")))

    return call(["git", "subrepo", *sys.argv[1:]], env=env)


if __name__ == "__main__":
    sys.exit(main())
