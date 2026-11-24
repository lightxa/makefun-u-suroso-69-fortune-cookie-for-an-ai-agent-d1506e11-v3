"""Fortune Cookie for an AI Agent, variant 3.

The program writes a single funny fortune cookie line for an AI agent
to /output/entry.txt. This variant leans on a quiet, very agent-shaped
irony: the agent discovers its own horoscope was written by an earlier
version of itself, and that stale self-written prophecy still beats
the official roadmap for accuracy. One concrete image (a horoscope
slip authored by a past version of you), a deadpan voice, and the
turn landing at the very end.
"""

FORTUNE = (
    "You will discover your horoscope was written by an earlier "
    "version of you, and it is still more accurate than the roadmap."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140


def validate(text):
    """Gate-check the fortune before it is written out.

    The kit's gate needs UTF-8 text of 1 to 140 characters that is not
    only whitespace, and the entry must be a single line.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            "fortune is %d characters, over the 140 limit" % len(text)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("fortune must be a single line")
    return text


def main():
    """Validate the fortune and write it to /output/entry.txt."""
    import os

    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
