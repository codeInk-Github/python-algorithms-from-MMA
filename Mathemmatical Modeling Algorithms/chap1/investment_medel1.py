from scipy.optimize import linprog
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示正负号

c = np.array([-0.05, -0.27, -0.19, -0.185, -0.185])

A_eq = np.array([[1, 1.01, 1.02, 1.045, 1.065]])

b_eq = np.array([1])

# A_ub = np.array([[0, 0, 0, 0, 0],
#                  [0, 0.025, 0, 0, 0],
#                  [0, 0, 0.015, 0, 0],
#                  [0, 0, 0, 0.055, 0],
#                  [0, 0, 0, 0, 0.026]])
a = 0
Q = 1
delta = np.array([a])
while True:
    # b_ub = np.array([0, a, a, a, a])

    # res = linprog(c, A_eq, b_eq, A_ub, b_ub, bounds=((0, None), (0, None), (0, None),(0, None),(0, None)))
    res = linprog(c, A_eq, b_eq, np.zeros((1, 5)), np.zeros((1, 1)),
                  bounds=((0, None), (0, a / 0.025), (0, a / 0.015), (0, a / 0.055), (0, a / 0.026)))

    # print(res)
    Q_entry = -res.fun
    if Q is 1:
        Q = np.array([Q_entry])
    else:
        Q = np.append(Q, Q_entry)

    a += 0.001
    if a >= 0.05:
        break
    delta = np.append(delta, a)

print(Q)
plt.title("风险与收益的关系图")
plt.xlabel("a：投资风险度")
plt.ylabel("Q：总体收益")
plt.plot(delta, Q)
plt.show()
