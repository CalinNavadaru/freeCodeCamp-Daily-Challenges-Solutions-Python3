def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    result = float(round((tank_size - fuel_level) * price_per_gallon, 2))
    integer_part = int(result)
    floating_part = int((result - integer_part) * 100)
    return "${}.{:0<2}".format(integer_part, floating_part)
