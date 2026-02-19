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

def mandelbrot_point_test():
    assert mandelbrot_point(0+0j, 100) == 100
    assert mandelbrot_point(-1+0j, 100) == 100
    assert mandelbrot_point(1+1j, 100) < 10
    assert mandelbrot_point(-0.75+0.1j, 1000) > 10



def compute_mandelbrot(width, height, x_min = -2, x_max = 1, y_min = -1.5, y_max = 1.5):

    mandelbrot_set = [[0 for _ in range(width)] for _ in range(height)]

    for j in range(height):
        for i in range(width):
            x = x_min + (x_max - x_min) * i / width
            y = y_min + (y_max - y_min) * j / height
            c = complex(x, y)
            mandelbrot_set[j][i] = mandelbrot_point(c, 1000)
    return mandelbrot_set

def compute_mandelbrot_test():
    
    grid = compute_mandelbrot(100, 100)
    
    assert len(grid) == 100          
    assert len(grid[0]) == 100       

    all_values = [value for row in grid for value in row]
    assert max(all_values) <= 1000   
    assert min(all_values) >= 0


if __name__ == "__main__":   
    compute_mandelbrot_test()
    print("All Mandelbrot tests passed")