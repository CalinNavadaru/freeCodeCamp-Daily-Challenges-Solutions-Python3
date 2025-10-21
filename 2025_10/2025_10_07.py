def find_landing_spot(matrix: list[list[int]]) -> list[int]:
    neighbors_index_list = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    min_danger = 9 * len(matrix) * len(matrix[0])
    min_i, min_j = -1, -1
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                danger = 0
                for x, y in neighbors_index_list:
                    if 0 <= i + x < len(matrix) and 0 <= j + y < len(matrix[i]):
                        danger += matrix[i + x][j + y]
                if danger < min_danger:
                    min_danger = danger
                    min_i = i
                    min_j = j
    return [min_i, min_j]
