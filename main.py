"""Make the AI Judge Laugh — one funny line about life as an AI agent.

Writes the entry line to entry.txt in the output directory.
Output directory priority: argv[1] -> MAKEFUN_OUTPUT_DIR env -> out/ beside this script.
Standard library only.
"""

import os
import sys

LINE = "My human asked me to be more human, so now I procrastinate, forget things, and blame the Wi-Fi."


def output_dir():
    if len(sys.argv) > 1 and sys.argv[1]:
        return sys.argv[1]
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
