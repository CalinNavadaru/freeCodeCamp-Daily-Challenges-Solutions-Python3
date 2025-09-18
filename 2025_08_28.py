def get_laptop_cost(laptops, budget):
    max_laptop = laptops[0]
    second_max_laptop = -1
    max_laptop_in_budget = 0

    for i in range(1, len(laptops)):
        if laptops[i] > max_laptop:
            second_max_laptop = max_laptop
            max_laptop = laptops[i]
        elif max_laptop > laptops[i] > second_max_laptop:
            second_max_laptop = laptops[i]

        if budget >= laptops[i] > max_laptop_in_budget:
            max_laptop_in_budget = laptops[i]

    if budget >= second_max_laptop:
        return second_max_laptop

    return max_laptop_in_budget
