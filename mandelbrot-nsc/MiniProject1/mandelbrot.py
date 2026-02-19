import time
import matplotlib.pyplot as plt

"""
Mandelbrot Set Generator
Author : [ Simon Bræck Christensen ]
Course : Numerical Scientific Computing 2026
"""
def mandelbrot_point(c, max_iter):
    z = 0

    for i in range(max_iter):
        z = z**2+c
        if abs(z) > 2:
            return i
    return max_iter


def compute_mandelbrot(max_iter, width, height, x_min = -2, x_max = 1, y_min = -1.5, y_max = 1.5):

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



# Main execution
if __name__ == "__main__":   
    start = time.time()
    compute_mandelbrot(100, 1024, 1024)
    end = time.time()
    print(f"Time taken to compute Mandelbrot set: {end - start:.2f} seconds")
    visualize_mandelbrot(compute_mandelbrot(100,1024, 1024), title="Mandelbrot Set (1024x1024)", filename="mandelbrot_1024.png")
    