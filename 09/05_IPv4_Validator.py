def is_valid_ipv4(ipv4):
    parts = ipv4.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            value = int(part)
        except ValueError:
            return False
        if part[0] == '0' and len(part) > 1 or not (0 <= value <= 255):
            return False
    return True

