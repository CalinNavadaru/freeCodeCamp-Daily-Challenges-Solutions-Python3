def dive(map_coordinates: list[list[str]], coordinates: list[int]) -> str:
    parts_not_found = 0
    x, y = coordinates
    for i in range(len(map_coordinates)):
        for j in range(len(map_coordinates[0])):
            if map_coordinates[i][j] == "O":
                parts_not_found += 1

    if map_coordinates[x][y] == "-":
        return "Empty"
    elif (map_coordinates[x][y] == "O" and parts_not_found == 1) or parts_not_found == 0:
        return "Recovered"

    return "Found"
