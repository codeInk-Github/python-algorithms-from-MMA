"""
说明：
"""

from scipy.optimize import linprog
import numpy as np

c = np.array([2, 3, 1])

print(c)
A_uq = np.array([[-1, -4, -2],
                 [-3, -2, -0]])

print(A_uq)
b_uq = np.array([-8, -6])

res = linprog(c, A_uq, b_uq, np.zeros((1, 3),int), np.zeros((1, 1), int), bounds=((0, None), (0, None), (0, None)))
print(res)
