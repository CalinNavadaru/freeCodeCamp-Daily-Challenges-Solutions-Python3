import re


def rgb_to_hex(rgb: str):
    values = re.match(r"rgb\((\d+), (\d+), (\d+)\)", rgb)

    r = hex(int(values.group(1)))[2:]
    g = hex(int(values.group(2)))[2:]
    b = hex(int(values.group(3)))[2:]

    return ("#" + r.rjust(2, "0") +
            g.rjust(2, "0") +
            b.rjust(2, "0"))
