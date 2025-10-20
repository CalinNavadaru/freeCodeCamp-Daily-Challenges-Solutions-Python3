def calculate_tips(meal_price: str, custom_tip: str) -> list[str]:
    price = float(meal_price[1:])
    custom_tip_value = int(custom_tip[0:len(custom_tip) - 1]) / 100
    tip_15 = round(price * 0.15, 2)
    tip_20 = round(price * 0.20, 2)
    tip_custom = round(price * custom_tip_value, 2)
    return [f"${str(tip_15).ljust(4, '0')}", f"${str(tip_20).ljust(4, '0')}", f"${str(tip_custom).ljust(4, '0')}"]
