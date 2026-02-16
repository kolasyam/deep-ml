import numpy as np

def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix to its Compressed Row Sparse (CSR) representation.

    :param dense_matrix: 2D list representing a dense matrix
    :return: A tuple containing (values array, column indices array, row pointer array)
    """
    
    values = []
    col_idx = []
    row_ptr = [0]

    non_zero_count = 0

    for row in dense_matrix:
        for j, val in enumerate(row):
            if val != 0:
                values.append(val)
                col_idx.append(j)
                non_zero_count += 1

        row_ptr.append(non_zero_count)

    return values, col_idx, row_ptr
