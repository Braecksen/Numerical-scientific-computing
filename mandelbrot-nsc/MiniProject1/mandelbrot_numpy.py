import time
import matplotlib.pyplot as plt
import statistics
import numpy as np


"""
Mandelbrot Set Generator
Author : [ Simon Bræck Christensen ]
Course : Numerical Scientific Computing 2026
"""


# Create the complex grid
x = np.linspace(-2, 1, 1024)
y = np.linspace(-1.5, 1.5, 1024)

X, Y = np.meshgrid(x, y)
C = X + 1j * Y


print (f" Shape : {C. shape }") # (1024 , 1024)
print (f" Type : {C. dtype }")





