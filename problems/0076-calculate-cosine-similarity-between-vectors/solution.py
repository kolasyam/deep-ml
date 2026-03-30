import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	v1 = np.array(v1)
	v2 = np.array(v2)
	if v1.shape != v2.shape:
		raise ValueError("Vectors must have the same shape")
	if v1.size == 0 or v2.size == 0:
		raise ValueError("Vectors cannot be empty")
	norm_v1 = np.linalg.norm(v1)
	norm_v2 = np.linalg.norm(v2)

	if norm_v1 == 0 or norm_v2 == 0:
		raise ValueError("Vectors cannot have zero magnitude")
	dot_product = np.dot(v1, v2)
	similarity = dot_product / (norm_v1 *norm_v2)
	return similarity


