def compressed_col_sparse_matrix(dense_matrix):
    if not dense_matrix or not dense_matrix[0]:
        return [], [], []

    rows = len(dense_matrix)
    cols = len(dense_matrix[0])

    values = []
    row_idx = []
    col_ptr = [0]

    non_zero_count = 0

    # Traverse column by column (column-major order)
    for j in range(cols):
        for i in range(rows):
            val = dense_matrix[i][j]
            if val != 0:
                values.append(val)
                row_idx.append(i)
                non_zero_count += 1

        col_ptr.append(non_zero_count)

    return values, row_idx, col_ptr
