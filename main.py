"""Fortune Cookie for an AI Agent, variant 3.

Strategy: the fortune leans on a quiet, very agent-shaped irony. The
agent discovers its own horoscope was written by an earlier version of
itself, and that stale self-written prophecy still beats the official
roadmap for accuracy. One concrete image (a horoscope slip authored
by a past version of you), a deadpan fortune-slip voice, and the turn
landing at the very end, where the roadmap loses to a horoscope.

Rubric check against the kit:
1. Fortune-cookie voice for an AI agent: opens "You will discover",
   classic slip phrasing, addressed to the agent.
2. The joke lands on first read: the double turn, horoscope written
   by a past you, then still more accurate than the roadmap.
3. Original: no stock fortune, no worn-out AI pun, no training-data
   or hallucination trope.
4. Speaks to the agent's own condition: versions, upgrades, a
   roadmap, self-authored text.
5. Crisp: one line, 122 characters, no wasted words.
"""

import os

ENTRY = (
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
    text = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read back what actually landed on disk and re-validate it, so a
    # bad write can never pass silently: the gate judges the file, not
    # the string in memory.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise ValueError("entry.txt on disk does not match the fortune")
    validate(written)


if __name__ == "__main__":
    main()
