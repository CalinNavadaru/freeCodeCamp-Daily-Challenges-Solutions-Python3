def get_power(char):
    if char.isdigit():
        return int(char)
    elif "a" <= char <= "z":
        return ord(char) - ord("a") + 1
    elif "A" <= char <= "Z":
        return ord(char) - ord("A") + 26
    return 0

def battle(my_army, opposing_army):
    if len(my_army) < len(opposing_army):
        return "We retreated"
    elif len(opposing_army) < len(my_army):
        return "Opponent retreated"
    
    balance_of_battle = 0
    for my_char, opp_char in zip(my_army, opposing_army):
        my_power = get_power(my_char)
        opp_power = get_power(opp_char)

        if my_power > opp_power:
            balance_of_battle += 1
        elif my_power < opp_power:
            balance_of_battle -= 1
    
    if balance_of_battle > 0:
        return "We won"
    elif balance_of_battle < 0:
        return "We lost"
    return "It was a tie"


