import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	A = np.array(A, dtype=float)
	T = np.array(T, dtype=float)
	S = np.array(S, dtype=float)
	if T.shape[0] != T.shape[1] or S.shape[0] != S.shape[1]:
		return -1
	if abs(np.linalg.det(T)) < 1e-9 or abs(np.linalg.det(S)) < 1e-9:
		return -1
	if T.shape[0] != A.shape[0] or A.shape[1] != S.shape[0]:
		return -1
	T_inv = np.linalg.inv(T)

	result = T_inv @ A @ S

	return result.tolist()