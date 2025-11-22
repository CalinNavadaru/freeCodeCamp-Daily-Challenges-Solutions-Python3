def generate_signature(name: str, title: str, company: str) -> str:
    if "A" <= name[0].upper() <= "I":
        prefix = ">>"
    elif "J" <= name[0].upper() <= "R":
        prefix = "--"
    else:
        prefix = "::"

    return f"{prefix}{name}, {title} at {company}"
