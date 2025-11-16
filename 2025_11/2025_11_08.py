def can_post(message: str) -> str:
    if len(message) <= 40:
        return "short post"

    if 40 < len(message) <= 80:
        return "long post"

    return "invalid post"
