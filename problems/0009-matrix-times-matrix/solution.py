import numpy as np

def matrixmul(A: list[list[int | float]],
              B: list[list[int | float]]) -> list[list[int | float]]:
    # a = np.array(a, dtype=float)
    # b = np.array(b, dtype=float)
    if not A or not B or not A[0] or not B[0]:
        return -1
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    if cols_A != rows_B:
        return -1
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_A):
            for k in range(cols_B):
                C[i][j] += A[i][k] * B[k][j]
    
    return C
