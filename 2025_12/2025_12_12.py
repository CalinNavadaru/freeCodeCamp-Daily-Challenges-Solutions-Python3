import collections

def update_inventory(inventory: list, shipment: list) -> list:

    ord_d = collections.OrderedDict([(e[1], e[0]) for e in inventory])
    for s in shipment:
        ord_d[s[1]] = ord_d.get(s[1], 0) + s[0]

    return [[e[1], e[0]] for e in ord_d.items()]