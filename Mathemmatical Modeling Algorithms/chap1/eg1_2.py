from scipy.optimize import linprog
import numpy as np

f = np.array([-2, -3, 5])
A_uq = np.array([[-2, 5, -1],
                 [1, 3, 1]])
b_uq = np.array([-10, 12])
A_eq = np.array([[1, 1, 1]])
b_eq = np.array([7])

# 求解函数
res = linprog(f, A_uq, b_uq, A_eq, b_eq, bounds=((0, None), (0, None), (0, None)))
# 目标函数最小值
print(res)
# 最优解
print(res.x)
