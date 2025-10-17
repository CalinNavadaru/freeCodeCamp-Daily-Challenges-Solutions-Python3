import re

def mask(card: str) -> str:
    if card[4] == '-':
        return "****-****-****-" + card[-4::1]

    return "**** **** **** " + card[-4::1]

print(mask("4012-8888-8888-1881"))