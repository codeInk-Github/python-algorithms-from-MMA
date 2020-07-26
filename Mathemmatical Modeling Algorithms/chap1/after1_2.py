"""
本问题与课本 例题1.3同一类型
"""

from scipy.optimize import linprog
import numpy as np

c = np.array([1, 1, 2, 2, 3, 3, 4, 4])

A_eq = np.array([[1, -1, -1, 1, -1, 1, 1, -1],
                 [1, -1, -1, 1, 1, -1, -3, 3],
                 [1, -1, -1, 1, -2, 2, 3, -3],
                 [0, 0, 0, 0, 0, 0, 0, 0]])

b_eq = np.array([0, 1, -1 / 2, 0])

res = linprog(c, None, None, A_eq, b_eq)

if res.success:
    x, z = - res.x[1::2] + res.x[::2], res.fun
    print("x:", x)
    print("z:", z)
else:
    print('linprog failed:', res.message)
