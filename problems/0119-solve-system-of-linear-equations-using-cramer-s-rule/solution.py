import numpy as np

def cramers_rule(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = A.shape[0]
    if A.shape[0]!=A.shape[1]:
        return -1
    det_A = np.linalg.det(A)
    
    if abs(det_A) < 1e-9:
        return -1
    x= np.zeros(n)
    
    for i in range(n):
        A_i = A.copy()
        A_i[:, i]= b
        det_Ai = np.linalg.det(A_i)
        x[i] = det_Ai / det_A
    return x