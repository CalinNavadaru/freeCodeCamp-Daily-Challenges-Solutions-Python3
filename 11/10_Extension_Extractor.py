import re


def get_extension(filename: str) -> str:
    extension = re.search(r"\.([^.]+)$", filename)

    if not extension:
        return "none"

    return extension.group()[1:]
