
def orthogonal_projection(v, L):
	dot_vL = sum(v[i] * L[i] for i in range(len(v)))
	dot_LL = sum(L[i] * L[i] for i in range(len(L)))

	if dot_LL == 0:
		return null
	scalar = dot_vL/dot_LL

	projection = [round(scalar * L[i], 3) for i in range(len(L))]
	return projection	
