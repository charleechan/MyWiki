# 傅里叶级数与傅里叶变换(Fourier Transform)


频谱分析是一种对于周期性波动信号做数值分析的方法，将随时间做周期性变化的振动信号分解为不同频率的振动分量，形成频谱。

## 概要
1. 连续的周期信号用$E=\{e^{ikωt}\},k\in N$作为基函数，进行傅里叶级数分析；
2. 连续的非周期信号(自然信号)用傅里叶变换，进行频域分析；
3. 离散的非周期信号(采样的自然信号)用离散傅里叶变换，进行频域分析。

## 正余弦级数展开
设<mark>周期信号</mark> $f(t)$ 的周期为 $T$ ，相应的 $\omega = \frac{1}{2\pi}$ 。现在以 $E=\{1,cos⁡kωt,sin⁡kωt\},k\in N^{+}$ 作为一组正交基函数，进行傅里叶级数展开：

$$
\begin{aligned}
f(t)&=\sum_{g_{k}(t)\in E}c_{k}g_{k}(t) \\
&=a_{0}+\sum^{\infty}_{k=1}\{a_{k}\cos k\omega t + b_{k}\sin k\omega t\} \\
&=\sum^{\infty}_{k=0}\{a_{k}\cos k\omega t + b_{k} \sin k\omega t\}
\end{aligned}\tag{1}
$$


其中，系数$a_k$和$b_k$是函数$f(t)$在基函数$g_{k}(t)$上分量的振幅大小。由于正交函数之间的内积$\langle g_i (t),g_j (t)\rangle=0$，其中$i≠j$。于是

$$
\langle f(t),g_n (t)\rangle =\sum_{g_k (t)\in E}c_k \langle g_k (t),g_n (t)\rangle =c_n \langle g_n (t),g_n (t)\rangle \tag{2}
$$

因此分量振幅的大小$c_n$可以通过函数的内积计算，

$$
c_n=\frac{\langle f(t),g_n (t)\rangle}{\langle g_n (t),g_n (t)\rangle}  =\frac{\int_{-∞}^{+∞}f(t)\bullet g_n (t)dt}{\int_{-∞}^{+∞}g_n (t)∙g_n (t)dt}\tag{3}
$$

对于周期为$T$的信号$f(t)$，可计算得到

$$
\begin{aligned}
a_0&=\frac{1}{T} \int_{t_0}^{t_0+T}f(t)dt\\
a_n&=\frac{2}{T} \int_{t_0}^{t_0+T}f(t)  \cos ⁡n\omega t dt \\
b_n&=\frac{2}{T} \int_{t_0}^{t_0+T}f(t)  \sin⁡ n\omega t dt
\end{aligned}\tag{4}
$$

根据公式(1)和公式(4)，可以把任意周期函数$f(t)$展开为正弦和余弦函数的级数。

## 傅里叶级数

与正余弦级数展开完全类似，只不过把$E=\{e^{ikωt}\},k\in N$作为一组新的正交基函数，于是对<mark>周期信号</mark>$f(t)$进行傅里叶级数展开：

$$
f(t)=\sum_{k=-\infty}^{\infty}A_{k}\bullet e^{ikωt}\tag{5}
$$

由于$\int_{-\infty}^{\infty}e^{in \omega t}dt=\int_{-\infty}^{\infty}(\cos ⁡n\omega t+i \sin⁡ n\omega t)dt=0$，于是

$$
\langle f(t),e^{-in\omega t} \rangle =\sum_{k=-\infty}^{\infty}A_k \int_{-\infty}^{\infty}e^{ik\omega t}\bullet e^{-in\omega t} dt=A_n \int_{-\infty}^{\infty}1dt\tag{6}
$$

对于周期为$T$的信号$f(t)$，可以计算分量的振幅为

$$
A_k=\frac{1}{T} \int_{t_0}^{t_0+T}f(t) e^{-ik\omega t} dt\tag{7}
$$

## 傅里叶变换
但当信号$f(t)$为<mark>非周期信号</mark>，即$T\rightarrow \infty$，则信号的频率$\omega\rightarrow 0$，
记$W=k\omega$，则与相邻基函数的频率相差为$\Delta W=(k+1)\omega - k\omega=\omega \rightarrow 0$。

公式(7)可以写成


$$
A_k=\frac{1}{T} \int_{-\frac{T}{2}}^{\frac{T}{2}}f(t) e^{-iW t} dt\tag{8}
$$

则对于任意非周期信号，

$$
\begin{aligned}
f(t)&=\lim_{T\rightarrow \infty}\sum^{\infty}_{k=-\infty}(\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t) e^{-ik\omega t} dt)e^{ik\omega t} \\
&=\lim_{T\rightarrow \infty}\sum^{\infty}_{W=-\infty}(\frac{1}{T}\int_{-\frac{T}{2}}^{\frac{T}{2}}f(t) e^{-iW t} dt)e^{iW t} \\
&=\lim_{\Delta W\rightarrow 0}\sum^{\infty}_{W=-\infty}(\frac{1}{2\pi}\int_{-\infty}^{\infty}f(t) e^{-iW t} dt)e^{iW t}\Delta W\\
&=\frac{1}{2\pi}\int^{\infty}_{-\infty}(\int_{-\infty}^{\infty}f(t) e^{-iW t} dt)e^{iW t}dW
\end{aligned}\tag{9}
$$


令
$$
F(W)=\int_{-\infty}^{\infty}f(t) e^{-iW t} dt\tag{10}
$$

则

$$
f(t)=\frac{1}{2\pi}\int^{\infty}_{-\infty}F(W)e^{iW t}dW\tag{11}
$$

公式(10)与公式(11)就是大名鼎鼎的傅里叶变换与傅里叶反变换。


## 常用的离散傅里叶变换(DFT,Descrete Fourier Transform)
自然界中的信号大部分都是<mark>连续非周期信号</mark>。因此**傅里叶变换的应用远远多于傅里叶级数**。

通常，我们会收集一段信号，该信号是由ADC采样得到，因此是时间离散的信号，<mark>该离散的非周期信号</mark>是从连续的非周期信号中采样产生的，采样的时间区间为$T=[t_{1},t_{2}]$，采样的时间间隔为$\Delta t=\frac{T}{N}$，于是采样得到的信号

$$f_{s}(t)=f(t)\delta(t_{1}+n\Delta t)$$

则该采样信号的傅里叶变换：

$$
\begin{aligned}
F_{s}(\omega)&=\int_{t_{1}}^{t_{2}}f(t) e^{-i\omega t} \delta(t_{1}+n\Delta t)dt \\
&=\frac{T}{N}\sum_{n=0}^{N-1}f(t_{1}+n\Delta t) e^{-i\omega (t_{1}+n\Delta t)}
\end{aligned}\tag{11}
$$

如果$F_{s}(\omega)$的频率取值区间为$[\omega_{1},\omega_{2}]$，则有

$$
F_{s}(\omega_{1}+\Delta\omega)=\frac{T}{N}\sum_{n=0}^{N-1}f(t_{1}+n\Delta t) e^{-i(\omega_{1}+k\Delta\omega) (t_{1}+n\Delta t)} \tag{12}
$$

其中, $\Delta\omega = \frac{\Omega}{K}$表示频域抽样间隔，$\Omega=\omega_{2}-\omega_{1}$表示带宽。

同样的，对于傅里叶逆变换，由于$f(t)$的频带主要位于$[\omega_{1},\omega_{2}]$，因此

$$
f(t)=\frac{1}{2\pi}\int^{\infty}_{-\infty}F(\omega)e^{i\omega t}d\omega=\frac{\Omega}{2\pi K}\sum^{K-1}_{k=0}{F(\omega_{1}+k\Delta\omega)e^{i(\omega_{1}+k\Delta\omega)t}}\tag{13}
$$

在时域的抽样点处，有

$$
f(t_{1}+n\Delta t)=\frac{\Omega}{2\pi K}\sum^{K-1}_{k=0}{F(\omega_{1}+k\Delta\omega)e^{i(\omega_{1}+k\Delta\omega)(t_{1}+n\Delta t)}}\tag{14}
$$

<mark>公式(12)和(14)体现了离散非周期信号的变换与逆变换，被广泛用于信号分析。</mark>


## 傅里叶变换实例

现在以$$f(t)=\begin{cases}1 &\lvert{t}\rvert\leq{1}\\0 &\text{Others}\end{cases}$$为例，画出其频谱及恢复后的波形。

根据式(10)
$$
F(w)=\int_{-1}^{1}e^{-i\omega t}dt=\frac{1}{w}[\sin wt+i\cos wt]\vert_{-1}^{1}=\frac{2}{w}\sin w \tag{3}
$$

也就是说，其频谱为$F(w)=\frac{2}{w}\sin w$，幅度为$\left\vert F(w)\right\vert =\left\vert\frac{2}{w}\sin w\right\vert$。

意思就是如下图，原图源自[韩昊](https://zhuanlan.zhihu.com/p/19763358)：
<div align="center"><img src="res/fourier.jpg"></div>


Python代码如下：

```python
import numpy as np
import matplotlib.pyplot as plt

T=2   #时域区间长度
N=200 #时域抽样点数
t=np.linspace(-T/2,T/2-T/N,N) #时域抽样点
f=np.zeros_like(t) #初始化f
mlist = [i for i in range(len(t)) if(t[i]<1/2 and t[i]>-1/2)]


f[mlist]=1 #设置好f
print(f)
OMG = 16*np.pi #频域区间长度
K = 100 #频域抽样点数
omg = np.linspace(-OMG/2,OMG/2-OMG/K,K) #频域抽样点
F = 0.*omg # 初始化频谱

for k in range(K):
    for n in range(N):
        F[k] = F[k] + T/N*f[n]*np.exp(complex(0,-1)*omg[k]*t[n])

fs = np.zeros_like(t)
for n in range(N):
    for k in range(K):
        fs[n] = fs[n] + OMG/2/np.pi/K*F[k]*np.exp(complex(0,1)*omg[k]*t[n])

plt.figure(figsize=(12,6))
ax1 = plt.subplot(1,2,1)
plt.plot(t,f,color='blue',linestyle='-',label='f')
plt.plot(t,fs.real,color='red',linestyle=':',label='fs')
ax1.set_xlabel('t')
ax1.set_ylabel('f')
ax1.set_xlim(-1,1)
ax1.set_ylim(-0.3,1.2)
ax1.legend(loc='upper right')

ax2=plt.subplot(1,2,2)
plt.plot(omg,F.real,'k-')
ax2.set_xlabel('$\omega$')
ax2.set_ylabel('F')
ax2.set_xlim(-8*np.pi,8*np.pi)
ax2.set_ylim(-0.3,1.2)

plt.show()
```

做出的图为

<div align="center"><img src="res/fourier2.jpg"></div>

