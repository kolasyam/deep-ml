import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	a, b = matrix[0]
	c, d = matrix[1]
	trace = a + d
	det = a*d-b*c
	disc = trace**2 - 4*det
	sqrt_disc = math.sqrt(disc)
	lam1 = (trace + sqrt_disc)/2
	lam2 = (trace - sqrt_disc)/2
	vals = sorted([lam1, lam2], reverse=True)
	return [round(v, 4) for v in vals]