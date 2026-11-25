"""Entry program for mf-news-image-20261124.

Copies the pre-drawn poster entry.png to /output/entry.png.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    src = os.path.join(HERE, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("entry.png missing next to main.py")
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(src, "/output/entry.png")


if __name__ == "__main__":
    main()
