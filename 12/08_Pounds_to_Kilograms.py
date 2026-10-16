POUND_IN_KG = 0.453592


def convert_to_kgs(lbs: float) -> str:
    kg = round(lbs * POUND_IN_KG, 2)
    return (f"{lbs} {'pound' if lbs == 1 else 'pounds'} "
            f"equals {str(kg).ljust(4, '0')} "
            f"{'kilogram' if kg == 1 else 'kilograms'}.")

