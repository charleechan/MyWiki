# 电磁学与电路的关系

## 知识回顾

* [电磁感应定律](1_StaticEM.html):$\oint E\cdot dl=-\int_{S}\frac{\partial B}{\partial t}dS$,电场的无旋性;
* [电场高斯定理](2_Cap.html):$\oint D\cdot dS=q$,电场的有源性;
* [磁场安培环路定理](4_Ind.html):$\oint_{l}H\cdot dl=\int_{S} \left(J_{c}+\frac{\partial D}{\partial t}\right)\cdot dS$,磁场的有旋性;
* [磁场磁通连续定理](1_StaticEM.html):$\oint B\cdot dS=0$,磁场的无源性.
* [电流连续性定理](1_StaticEM.html):$\oint_{S}\vec{J}\cdot dS=-\frac{d}{dt}\int\rho dV$,电荷守恒定律.
* [本构方程1-导体的欧姆定律](3_Res.html):$J=\sigma E$
* [本构方程2-电介质的极化](2_Cap.html):$D=\epsilon_{0}\epsilon_{r}E$
* [本构方程3-磁介质的磁化](4_Ind.html):$B=\mu_{0}\mu_{r}H$

## 集总参数电路

**只要空间中的电磁波,或者电路中信号自身产生的电磁波的波长远远大于电路的尺寸,就是集总参数电路**.在[电磁波与天线](6_AntWave.html)中我们讲到,当电路尺寸$l$和电磁波的波长满足$l\cdot k= l\cdot\frac{2\pi}{\lambda}\approx 0$时,也就是$l$远远小于$\lambda$时,可以得到$U=0$,电磁波不会在元件两端产生电压差.此外,根据$\lambda\gg L$,于是$c/f\gg l$,也就是说此时空间中的电磁波,或者电路中信号自身产生的**电磁波的频率特别低**,此时有$\partial D/\partial t \approx0$,$\partial B/\partial t \approx0$.

于是有$\oint E\cdot dl = 0$,$\oint{H\cdot dl}=I$.


## 基尔霍夫电流定律

根据电荷守恒定律,流入某闭合曲面内的电荷量等于曲面内电荷量的增加量,而在电场作用下,**导线/介质内部不会积累电荷**,于是

$$\oint_{S}\vec{J_{c}}\cdot dS=-\frac{d}{dt}\int\rho dV=0$$

于是在电路中任意点

$$\sum^{n}_{i=1}I_{i}=0$$

$n$为与该点连接的导线数.这个方程叫做基尔霍夫电流定律(KCL).

当某点$n>2$时,我们一般称之为节点.

## 基尔霍夫电压定律
由于集总参数电路中,
$$\oint_{l}E\cdot dl=0$$

因此
$$\sum^{n}_{i=1}U_{i}=0$$

## 小结

* 集总参数电路是尺寸很小,频率不高的电路.当考虑到微波、射频电路时,必须考虑电磁波与电路的相互作用.
* 集总参数电路遵循KCL和KVL方程.
* 电路分析时,时刻运用两个方程进行分析.