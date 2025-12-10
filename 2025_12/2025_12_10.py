import re


def parse_bold(markdown: str) -> str:
    return re.sub(r"(\*\*|__)(\S[^*_]*\S)(\*\*|__)", r"<b>\2</b>", markdown)
