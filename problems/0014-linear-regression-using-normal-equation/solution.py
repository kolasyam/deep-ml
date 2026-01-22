import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    # Your code here, make sure to round
    X = np.array(X , dtype=float)
    Y = np.array(y, dtype=float)
    Xt = X.T
    theta = np.linalg.inv(Xt @ X) @ Xt @ Y
    theta = np.round(theta, 4)
    return theta