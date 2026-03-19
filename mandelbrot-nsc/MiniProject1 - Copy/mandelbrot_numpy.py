import time
import matplotlib.pyplot as plt
import statistics
import numpy as np


"""
Mandelbrot Set Generator
Author : [ Simon Bræck Christensen ]
Course : Numerical Scientific Computing 2026
"""

def compute_mandelbrot_numpy(max_iter, width, height, x_min = -2, x_max = 1, y_min = -1.5, y_max = 1.5):
    # Create the complex grid
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)

    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y

    # Initialize Z and M
    Z = np.zeros_like(C, dtype=np.complex128)   
    M = np.zeros(C.shape, dtype=int)            

    for n in range(max_iter):
        mask = np.abs(Z) <= 2
        if not mask.any():
            break
        Z[mask] = Z[mask]**2 + C[mask]
        M[mask] += 1

    return M



def benchmark(func, *args, n_runs=3):
    """Time func, return median runtime and result."""
    times = []

    for _ in range(n_runs):
        t0 = time.perf_counter()
        result = func(*args)
        times.append(time.perf_counter() - t0)

    median_t = statistics.median(times)
    print(
        f"Median: {median_t:.4f}s "
        f"(min={min(times):.4f}, max={max(times):.4f})"
    )

    return median_t, result


# Main execution
if __name__ == "__main__":   

    t, M = benchmark(compute_mandelbrot_numpy,100, 1024, 1024, n_runs=3)
    plt.imshow(M, cmap="inferno", extent=(-2, 1, -1.5, 1.5))
    plt.colorbar(label="Iterations")
    plt.title("Mandelbrot Set")
    plt.show()