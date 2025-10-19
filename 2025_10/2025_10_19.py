import re


def extract_attributes(element: str) -> list[str]:
    results = re.findall(r"[a-zA-Z]+=\"[a-zA-Z0-9_\- ]+\"", element)
    return [", ".join([x.strip('" ') for x in result.split("=")]) for result in results]
