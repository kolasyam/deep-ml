def find_treasure(start_x: float) -> float:
    # 🔴 Fix 1: avoid bad starting region
    x = start_x if start_x > 0 else 1.0

    learning_rate = 0.01
    tolerance = 1e-6
    max_iters = 10000

    for _ in range(max_iters):
        grad = 4 * (x ** 3) - 9 * (x ** 2)

        new_x = x - learning_rate * grad

        # convergence check
        if abs(new_x - x) < tolerance:
            break

        x = new_x

    return x