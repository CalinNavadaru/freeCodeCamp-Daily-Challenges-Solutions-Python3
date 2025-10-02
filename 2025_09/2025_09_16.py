import re


def capitalize(paragraph):
    paragraph = paragraph.capitalize()

    def __capitalize(match):
        periods = match.group(1)
        whitespaces = match.group(2)
        first_letter = match.group(3)

        return periods + whitespaces + first_letter.upper()

    return re.sub(r"([.?!])(\s*)([a-zA-Z])", __capitalize, paragraph)
