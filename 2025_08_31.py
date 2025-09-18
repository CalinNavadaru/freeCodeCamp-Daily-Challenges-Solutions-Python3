d = {"red": 255, "blue": 255, "green": 255}


def generate_hex(color):
    global d
    if color not in ["red", "blue", "green"]:
        return "Invalid color"
    if color == "red":
        generated_hex = f"{hex(d['red']).upper()[2:]}0000"
        d['red'] -= 1
        if d['red'] == 1:
            d['red'] = 255
        return generated_hex
    if color == "blue":
        generated_hex = f"0000{hex(d['blue']).upper()[2:]}"
        d['blue'] -= 1
        if d['blue'] == 1:
            d['blue'] = 255
        return generated_hex

    generated_hex = f"00{hex(d['green']).upper()[2:]}00"
    d['green'] -= 1
    if d['green'] == 1:
        d['green'] = 255
    return generated_hex
