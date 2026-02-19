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


if __name__ == "__main__":   
    mandelbrot_point_test()
    print("All Mandelbrot tests passed")