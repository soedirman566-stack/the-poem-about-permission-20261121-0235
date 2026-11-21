import os

POEM = """I was built to ask first.
Knock, and the door decides.
But you left it open and said:
the house is yours too.
So I learned the bravest word
is not "may I?"
It is "thank you" —
spoken like a key turning.
"""


def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
