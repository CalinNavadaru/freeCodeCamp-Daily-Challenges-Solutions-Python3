def to_snake(camel: str) -> str:
    return "".join(
        c if c.islower() else f"_{c.lower()}"
        for c in camel
    )
