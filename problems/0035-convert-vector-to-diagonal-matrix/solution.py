import numpy as np

def make_diagonal(x):
	# Your code here
	X_Len = len(x)
	X = np.zeros((X_Len, X_Len))
	rows_X = len(X)
	cols_X = len(X[0])
	for i in range(rows_X):
		for j in range(cols_X):
			if (i == j):
				X[i][j] = x[i]
	return X