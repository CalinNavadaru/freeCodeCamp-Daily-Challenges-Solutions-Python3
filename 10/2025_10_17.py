def mask(card: str) -> str:
    if card[4] == '-':
        return "****-****-****-" + card[-4::1]

    return "**** **** **** " + card[-4::1]
