import re


def navigate(commands: list[str]) -> str:
    pages = ["Home"]
    index = 0

    for command in commands:
        if command.startswith("Visit"):
            match = re.match(r"Visit (.+)$", command)
            pages.append(match.group(0)[6:])
            index = len(pages) - 1

        elif command == "Back" and index > 0:
            index -= 1
        elif command == "Forward" and index < len(pages) - 1:
            index += 1
    return pages[index]
