#!/usr/bin/env python3
"""Sum up 25 November's world news in one image — a make.fun entry.

The program copies the poster image held in this repository to
/output/entry.png, where the competition's sealed scorer reads it.
"""

import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
OUTPUT = Path("/output/entry.png")


def copy_poster() -> None:
    assert SOURCE.is_file(), "poster image is missing"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, OUTPUT)


if __name__ == "__main__":
    copy_poster()
