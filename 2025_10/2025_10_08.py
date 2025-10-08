import math

def goldilocks_zone(mass: float):

    sqrt_luminosity = math.sqrt(mass ** 3.5)
    return [round(0.95 * sqrt_luminosity, 2), round(1.37 * sqrt_luminosity, 2)]