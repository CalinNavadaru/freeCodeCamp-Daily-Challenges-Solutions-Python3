import re


def validate(email: str) -> bool:
    result = re.fullmatch(r"^[^@.]([.][a-zA-Z0-9_-]|[a-zA-Z0-9_-])*@([^.@]+\.)+[a-zA-Z]{2,}$", email)

    return result is not None
