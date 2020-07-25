"""
在这个例子中，设计了两个函数
model1：   用来对整体的趋势做一个展示
select_x： 用来查询在给定的条件下，x向量的各个值
"""
from scipy.optimize import linprog
import numpy as np
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示正负号


def model1(a_max, step, M):
    """

    :param a_max: 最大能接受的风险
    :param M: 投入的资金总额
    :return: 显示出在风险已知的情况下，可以获得的最大总体收益
    """
    c = np.array([-0.05, -0.27, -0.19, -0.185, -0.185])

    A_eq = np.array([[1, 1.01, 1.02, 1.045, 1.065]])

    b_eq = np.array([M])

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
                      bounds=((0, None), (0, (M * a) / 0.025),
                              (0, (M * a) / 0.015), (0, (M * a) / 0.055),
                              (0, (M * a) / 0.026)))

        # print(res)
        Q_entry = -res.fun
        if Q is 1:
            Q = np.array([Q_entry])
        else:
            Q = np.append(Q, Q_entry)

        a += step
        if a >= 0.05:
            break
        delta = np.append(delta, a)

    print(Q)
    plt.title("风险与收益的关系图")
    plt.xlabel("a：投资风险度")
    plt.ylabel("Q：总体收益")
    plt.plot(delta, Q)
    plt.show()


def select_x(a, M):
    c = np.array([-0.05, -0.27, -0.19, -0.185, -0.185])

    A_eq = np.array([[1, 1.01, 1.02, 1.045, 1.065]])

    b_eq = np.array([M])

    res = linprog(c, A_eq, b_eq, np.zeros((1, 5)), np.zeros((1, 1)),
                  bounds=((0, None), (0, (M * a) / 0.025),
                          (0, (M * a) / 0.015), (0, (M * a) / 0.055),
                          (0, (M * a) / 0.026)))

    print("在给定的参数下，")
    print("x0:", res.x[0])
    print("x1:", res.x[1])
    print("x2:", res.x[2])
    print("x3:", res.x[3])
    print("x4:", res.x[4])

# model1(0.5, 0.001, 1)
# select_x(0.006, 1)
