import time
import matplotlib.pyplot as plt
import statistics


"""
Mandelbrot Set Generator
Author : [ Simon Bræck Christensen ]
Course : Numerical Scientific Computing 2026
"""
def mandelbrot_point(c, max_iter):
    z = 0

    for i in range(max_iter):
        z = z = z*z + c
        if abs(z) > 2:
            return i
    return max_iter


def compute_mandelbrot_naive(max_iter, width, height, x_min = -2, x_max = 1, y_min = -1.5, y_max = 1.5):

    mandelbrot_set = [[0 for _ in range(width)] for _ in range(height)]

    for j in range(height):
        for i in range(width):
            x = x_min + (x_max - x_min) * i / width
            y = y_min + (y_max - y_min) * j / height
            c = complex(x, y)
            mandelbrot_set[j][i] = mandelbrot_point(c, max_iter)
    return mandelbrot_set


##### Visualization function made with claude AI!!! #####
def visualize_mandelbrot(grid, title="Mandelbrot Set", cmap="hot", filename="mandelbrot.png"):
    plt.figure(figsize=(8, 6))
    
    # imshow can accept a 2D list directly
    plt.imshow(grid, extent=[-2, 1, -1.5, 1.5], origin='lower', cmap=cmap)
    
    plt.colorbar(label="Iteration count")
    plt.title(title)
    plt.xlabel("Real axis")
    plt.ylabel("Imaginary axis")
    
    plt.savefig(filename)
    plt.show()

    

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

    t, M = benchmark(compute_mandelbrot_naive,100, 1024, 1024, n_runs=3)