from scipy.optimize import linprog
import numpy as np

c = np.array([-3, 1, 1])

A_eq = np.array([[-2, 0, 1]])

b_eq = np.array([1])

A_ub = np.array([[1, -2, 1],
                 [4, -1, -2]])

b_ub = np.array([11, -3])

res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=((0, None), (0, None), (0, None)))

print(res)
z = -res.fun
x = np.round(np.array(res.x)).astype(int)
print("x:", x)
print("z:", z)
