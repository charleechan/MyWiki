# -*- using: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt


def sigGen(t, mode=0):
    """
    return a signal combined by 10Hz, 25Hz, 50Hz, 100Hz

    Paras:
    t: list of the time sample points
    mode:
        0-superpose叠加
        1-positive sequence正序
        2-negative sequence倒序
    """
    # T = t[-1] - t[0]
    N = len(t)
    x = np.zeros_like(t)

    x1 = np.cos(2 * np.pi * 10 * t)
    x2 = np.cos(2 * np.pi * 25 * t)
    x3 = np.cos(2 * np.pi * 50 * t)
    x4 = np.cos(2 * np.pi * 100 * t)
    t1 = [i for i in range(len(t)) if i < (N - 1) / 4]
    t2 = [i for i in range(len(t)) if i >= (N - 1) / 4 and i < (N - 1) / 2]
    t3 = [i for i in range(len(t)) if i >= (N - 1) / 2 and i < 3 * (N - 1) / 4]
    t4 = [i for i in range(len(t)) if i >= 3 * (N - 1) / 4]

    if mode == 0:
        x = x1 + x2 + x3 + x4
    elif mode == 1:
        x1[t2] = 0
        x1[t3] = 0
        x1[t4] = 0
        x2[t1] = 0
        x2[t3] = 0
        x2[t4] = 0
        x3[t1] = 0
        x3[t2] = 0
        x3[t4] = 0
        x4[t1] = 0
        x4[t2] = 0
        x4[t3] = 0
        x = x1 + x2 + x3 + x4
    elif mode == 2:
        x4[t2] = 0
        x4[t3] = 0
        x4[t4] = 0
        x3[t1] = 0
        x3[t3] = 0
        x3[t4] = 0
        x2[t1] = 0
        x2[t2] = 0
        x2[t4] = 0
        x1[t1] = 0
        x1[t2] = 0
        x1[t3] = 0
        x = x1 + x2 + x3 + x4
    return x


def main():
    T = 1  # 时间长度为1s
    fs = 1000  # 采样率为1000
    t = np.linspace(0, T, fs + 1)
    x = sigGen(t, 2)
    plt.figure()
    plt.plot(t, x)
    plt.show()


if __name__ == "__main__":
    main()
