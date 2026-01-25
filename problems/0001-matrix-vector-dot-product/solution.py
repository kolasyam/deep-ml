def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if not a or not a[0]:
		return -1
	rows = len(a)
	cols = len(a[0])
	if cols != len(b):
		return -1
	results =[]
	for i in range(rows):
		dot = 0
		for j in range(cols):
			dot += a[i][j] * b[j]
		results.append(dot);
	return results