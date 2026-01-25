def transpose_matrix(matrix: list[list[int|float]]) -> list[list[int|float]]:
    rows = len(matrix)
    cols = len(matrix[0])

    result = []
    for j in range(cols):
        column = []
        for i in range(rows):
            column.append(matrix[i][j])
        result.append(column)

    return result      