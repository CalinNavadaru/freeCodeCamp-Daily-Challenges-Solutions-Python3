import re


def strip_tags(html: str) -> str:
    content = re.findall(r">([^<]+)<", html)
    return "".join(content)
