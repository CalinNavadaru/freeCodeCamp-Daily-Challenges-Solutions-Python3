def rotate(matrix: list[list[int]]) -> list[list[int]]:
    # transpose the matrix
    for i in range(0, len(matrix)):
        for j in range(0, i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(0, len(matrix)):
        for j in range(0, i // 2 + 1):
            matrix[i][j], matrix[i][len(matrix[i]) - 1 - j] = matrix[i][len(matrix[i]) - 1 - j], matrix[i][j]
    return matrix
