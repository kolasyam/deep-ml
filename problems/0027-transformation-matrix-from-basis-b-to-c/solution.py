import numpy as np
def transform_basis(B: list[list[int]], C: list[list[int]]) -> list[list[float]]:
	B = np.array(B, dtype=float)
	C = np.array(C, dtype=float)
	C_inv = np.linalg.inv(C)
	P = (C_inv @ B)
	P_rounded = np.round(P, 4)
	return P_rounded.tolist()