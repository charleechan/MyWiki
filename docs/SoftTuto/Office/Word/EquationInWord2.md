# 跨行对齐公式与公式代码

## 跨行对齐公式
1. 打开或新建一个Word文档，按`Alt`+`=`键，插入一个新的公式，公式菜单默认使用`Unicode`模式；
2. 输入`\eqarray<space>`, 出现一个黑色实心方块；
3. 输入`(a+b&=c@b+c+1&=d)`,然后按`<空格>`，可以看到公式已经完整出现.

> LaTeX公式代码为`A=\{\matrix{a&b&c\\d&e&f\\g&h&j}\}`。

<mark>强烈建议使用Latex公式编码</mark>, [Latex公式大全](/Coding/LangsMark/MD/EquationInMD.html))

## Latex公式代码

[查询Word官网](https://support.microsoft.com/zh-cn/office/word-%E4%B8%AD%E4%BD%BF%E7%94%A8-unicodemath-%E5%92%8C-latex-%E7%9A%84%E7%BA%BF%E6%80%A7%E6%A0%BC%E5%BC%8F%E5%85%AC%E5%BC%8F-2e00618d-b1fd-49d8-8cb4-8d17f25754f8)可以得到，Word中的Latex公式主要有以下几点不同:

1. 不支持`\begin{}`和`\end{}`，因此要将
   * `\begin{matrix}***\end{matrix}` 修改为 `\matrix{***}`
   * `\begin{cases}***\end{cases}` 修改为 `\cases{***}`
2. 花括号写起来更简单，不需要写成`\left\{`，直接使用`{`即可；
3. 绝对值符号写起来更简单，不需要写成`\left\vert`或`\vert`，直接使用`|`；
4. 不支持关键字`\boxed{}`，直接使用`\rect{}`。

下面列出了Word中常用的公式：

|公式效果|Word中Latex代码|Markdown中公式代码|
|:-:|:-:|:-:|
|$\overrightarrow{abc}$|`\vec{abc}`|`\overrightarrow{abc}`|
|$\widehat{abc}$|`\hat{abc}`|`\widehat{abc}`|
|$\overline{abc}$|`\overbar{abc}`|`\overline{abc}`|
|$\overbrace{abc}$|`\overbrace{abc}`|`\overbrace{abc}`|
|$\left\{a+\frac{b}{c}\right\}$|`\left{a+\frac{b}{c}\right}`|`\left\{a+\frac{b}{c}\right\}`|
|$\left(a+\frac{b}{c}\right)$|`\left(a+\frac{b}{c}\right)`|`\left(a+\frac{b}{c}\right)`|
|$\left\{\frac{b}{c}\left\vert x+y\right\vert\right\}$|<span style="font-family:Consolas; background:#eee; color:#000">\\left{\\frac{b}{c}&#124;x+y&#124;\\right}</span>|`\left\{\frac{b}{c}\left\vert x+y\right\vert\right\}`|
|$\frac{b}{a+c}$|`\frac{b}{a+c}`|`\frac{b}{a+c}`|
|${_a^b}x{_c^d}$|`{_a^b}x{_c^d}`|`{_a^b}x{_c^d}`|
|$\lim_{n\rightarrow\infty}{n}$|`\lim\below{n\rightarrow\infty}{n}`|`\lim_{n\rightarrow\infty}{n}`|
|$\begin{matrix}a&b&\cr&c&d\cr\end{matrix}$|`\matrix{a&b&\cr&c&d\cr}`|`\begin{matrix}a&b&\cr&c&d\cr\end{matrix}`|
|$\iint_{a=0}^{\infty}{a}$|`\iint_{a=0}^{\infty}{a}`|`\iint_{a=0}^{\infty}{a}`|
|$\sqrt[5]{a^2}$|`\sqrt[5]{a^2}`|`\sqrt[5]{a^2}`|


