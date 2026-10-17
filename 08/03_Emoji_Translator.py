TRANSLATION_TABLE = {
    "👶": "baby",
    "🐱": "cat",
    "🐕": "dog",
    "🐟": "fish",
    "🥵": "hot",
    "🧊": "ice",
    "🪨": "rock",
    "🦈": "shark",
    "🍲": "soup",
    "⭐": "star"
}


def get_emoji_phrase(s: str) -> str:
    return " ".join(TRANSLATION_TABLE[word] for word in s.strip())
