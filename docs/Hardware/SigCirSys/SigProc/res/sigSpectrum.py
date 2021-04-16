# -*- using: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import inspect
import os


def main():
    currentdir = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    os.sys.path.insert(0, parentdir)

    from res.sigGen import sigGen

    T = 1  # 时间长度为1s
    fs = 1000  # 采样率为1000,决定了时域信号的时间分辨率
    t = np.linspace(0, T, fs + 1)
    plt.figure(figsize=(12, 12))

    for i in range(3):
        # generate a signal combined by 10Hz, 25Hz, 50Hz, 100Hz
        x = sigGen(t, i)

        Amplitude = abs(np.fft.fft(x))
        n = x.size
        sampleDeltaTime = 1/fs # 时域的采样间隔时间
        freq = np.fft.fftfreq(n, d=sampleDeltaTime)

        ax1 = plt.subplot(3, 2, i*2+1)
        plt.plot(t, x, color='blue', linestyle='-', label='$x$')
        ax1.set_xlabel('$t(s)$')
        ax1.set_ylabel('$x(V)$')
        ax1.legend(loc='upper right')

        ax2 = plt.subplot(3, 2, i*2+2)
        plt.plot(freq[0:int(T*fs/3)], Amplitude[0:int(T*fs/3)], 'k-')
        ax2.set_xlabel('$f(Hz)$')
        ax2.set_ylabel('$Amplitude/V$')
    plt.show()


if __name__ == "__main__":
    main()
