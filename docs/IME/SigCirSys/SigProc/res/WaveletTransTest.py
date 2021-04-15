import numpy as np
import matplotlib.pyplot as plt
import os, inspect
import math


def main():
    currentdir = os.path.dirname(
        os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    os.sys.path.insert(0, parentdir)

    from res.WaveletTrans import Wavelet

    waveletn = 256
    wavelettest = Wavelet(waveletn)
    t = np.linspace(0, 255, 256)
    waveletorigindata = np.sin(t) * np.exp(-((t - 100) / 50)**2) + 1

    filterFlag = 0  # 滤波方式: 1-按能量滤波; 0-按频率滤波
    if (filterFlag):
        # 按能量大小进行滤波，滤掉将能量较小的分量
        # 将小波系数进行降序排列(升序取反)
        plt.figure(figsize=(12, 10))
        for k in range(4):
            waveletdata = np.sin(t) * np.exp(-((t - 100) / 50)**2) + 1
            wavelettest.transform_forward(waveletdata, 1)  # 执行小波变换
            waveletnc = 20 * (2**k)  # 按能量滤波时，保留的分量数
            newdata = sorted(waveletdata,
                             key=lambda ele: abs(ele),
                             reverse=True)
            for i in range(waveletnc, waveletn):  # 将能量较小的分量直接置0，删除啦
                for j in range(0, waveletn):
                    if (abs(newdata[i] - waveletdata[j]) < 1e-6):
                        waveletdata[j] = 0.0
                        break
            wavelettest.transform_inverse(waveletdata, 1)

            waveleterr = 0.0
            for i in range(0, waveletn):
                waveleterr += abs(waveletorigindata[i] - waveletdata[i]) / abs(
                    waveletorigindata[i])
            ax = plt.subplot(2, 2, k + 1)
            plt.plot(waveletorigindata,
                     color='blue',
                     linestyle='-',
                     label='$f$')
            plt.plot(waveletdata, color='red', linestyle='-', label="$f'$")
            ax.set_xlabel('$t(s)$')
            ax.set_ylabel('$f(V)$')
            ax.legend(loc='upper right')
            ax.set_title("waveletnc:{},relative error:{:.3f}".format(
                waveletnc, waveleterr / waveletn))
        plt.show()
    else:
        # 按频率分量进行滤波,带通滤波器，可以滤除高频或(/和)低频分量
        # 这里去除低频分量,实现去除基线
        plt.figure(figsize=(12, 10))
        lFreq = [0, 0.2, 0, 0.05]  # 按频率滤波时，相对低截止频率
        hFreq = [1, 1, 0.5, 0.9]  # 按频率滤波时，相对高截止频率
        for k in range(len(hFreq)):
            waveletdata = np.sin(t) * np.exp(-((t - 100) / 50)**2) + 1
            wavelettest.transform_forward(waveletdata, 1)  # 执行小波变换
            omg = [
                i for i in range(len(waveletdata)) if i < len(waveletdata) *
                lFreq[k] or i > len(waveletdata) * hFreq[k]
            ]
            waveletdata[omg] = 0
            wavelettest.transform_inverse(waveletdata, 1)

            waveleterr = 0.0
            for i in range(0, waveletn):
                waveleterr += abs(waveletorigindata[i] - waveletdata[i]) / abs(
                    waveletorigindata[i])
            ax = plt.subplot(2, 2, k + 1)
            plt.plot(waveletorigindata,
                     color='blue',
                     linestyle='-',
                     label='$f$')
            plt.plot(waveletdata, color='red', linestyle='-', label="$f'$")
            ax.set_xlabel('$t(s)$')
            ax.set_ylabel('$f(V)$')
            ax.legend(loc='upper right')
            ax.set_title(
                "BandPass[{:.2f},{:.2f}],relative error:{:.3f}".format(
                    lFreq[k], hFreq[k], waveleterr / waveletn))
        plt.show()


if __name__ == "__main__":
    main()