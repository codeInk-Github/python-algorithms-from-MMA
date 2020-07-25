"""
本问题属于通过变换转化为线性规划的题目，
将原先的4变量
"""

from scipy.optimize import linprog
import numpy as np

c = np.array([1, 1, 2, 2, 3, 3, 4, 4])

A_ub = np.array([[1, -1, -1, 1, -1, 1, 1, -1],
                 [1, -1, -1, 1, 1, -1, -3, 3],
                 [1, -1, -1, 1, -2, 2, 3, -3]])

b_ub = np.array([-2, -1, -1 / 2])

res = linprog(c, A_ub, b_ub, np.zeros((1, 8)), np.zeros((1, 1)))

# print(res)
x, z = res.x[1::2] - res.x[::2], res.fun
print("x:", x)
print("z:", z)
