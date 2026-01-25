def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if not matrix or not matrix[0]:
		return []
	rows = len(matrix)
	cols = len(matrix[0])
	mean = []
	if mode == "row":
		for i in range(rows):
			mean.append(sum(matrix[i])/cols)
	elif mode == "column":
		for j in range(cols):
			cols = 0
			for i in range(rows):
				cols += matrix[i][j]
			mean.append(cols/rows)
	else:
		return []		
	return mean						