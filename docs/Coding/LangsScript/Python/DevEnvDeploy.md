# Python开发环境的配置

## Python简介

1. Python是一种脚本语言，脚本文件名后缀为`.py`；

2. 与C语言不同，它不需要编译链接的过程，而是由一个应用程序直接对代码进行解释，然后执行；这个用来解释脚本代码并执行的应用程序叫做`解释器`。

3. 通常，为了代码可读性，把一个很长的脚本文件分成多个脚本文件，几个脚本组合成一个软件包，叫做**模块**。一个模块一般是一个文件夹。

4. 有许多通用的模块，会随着Python的**官方版本**发布，形成**内置模块**。

5. 还有一些用处比较专业的模块，就是**第三方模块**，一般使用`PIP`进行第三方模块的**安装，更新，卸载**等。

笔者推荐使用 `VScode` 进行 `Python` 程序的开发。

环境系统：`Windows 10 x64 Enterprise`。

## 下载并安装便携版Python
1. 去[Python官网](https://www.python.org/downloads/windows/)，在左侧`Stable Releases`一栏下载Python的可移植包**Windows x86-64 embeddable zip file**，根据需要选择Python版本，这里下载的是`python-3.6.8-embed-amd64.zip`，大小只有不到7MB。


2. 安装Python：解压 `zip` 文件到你想安装的路径，重命名文件夹为`Python`,可以看到其中已经有一个 `python.exe` ，在CMD中定位到此`Python`文件夹，输入`python`后按回车，进入`python`命令行环境，输入以下命令:

   ```python
   import sys
   print('hello, python!')
   print(sys.path)
   ```

   按回车，`print(sys.path)`可以看到Python `模块`的路径，包括了`python36.zip`及本程序的目录`Python`。

   > 双击打开`python36.zip`，可以看到其中已经内置了一些基本的模块，包括`json`,`html`等。

3. 设置环境变量`PATH`：添加该`Python`目录到**系统环境变量**`Path`(或`PATH`，不区分大小写)。

   > 设置环境变量之后，以后在任意路径打开命令行，输入`python`，都会调用该PATH中包含的路径下的`python.exe`。如果没有打开Python命令行，你需要重启系统以更新环境变量的设置。

5. 你也可以把步骤2中的代码写入一个脚本文件`hello.py`，然后在该脚本文件所在路径打开命令行，执行`python hello.py`，让`解释器`执行该脚本。


## 安装第三方Python模块


1. **安装模块管理工具PIP**:下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)或[get-pip.py](res/get-pip.py)到文件夹`Python`中，在CMD中定位到此`Python`文件夹,运行`python get-pip.py`，安装完成后修改python36._pth的内容为：

   ```
   python36.zip
   .
   # Uncomment to run site.main() automatically
   import site
   ```
   > 该文件中定义了python解释器的搜索路径，包括 python36.zip文件包，`.`表示当前路径，以及`site`指定的路径。
   > **可以在此文件中任意添加路径,以包含你自定义的包,因此遇到*ModuleNotFoundError: No module named*错误时,可尝试修改此文件**.

2. 可以看到`Python/Scripts`目录下已经有`pip.exe`等几个`pip`应用程序。把该`Python/Scripts`目录也添加到系统环境变量`PATH`。

3. **安装第三方模块**：使用`pip`管理python软件包，直接在cmd窗口中输入pip命令，会显示pip所有的参数使用方法；

模块的安装包文件名是`.whl`,你可以去以下站点下载要安装的包

* [Python Package Index](https://pypi.org)
* [清华镜像站](https://pypi.tuna.tsinghua.edu.cn/simple/)
* [阿里镜像源](http://mirrors.aliyun.com/pypi/simple/)

以下是常用的`pip`命令：

```bash
pip install [PackageName]                # 安装某个模块
pip install [PackageName]==[VersionNum]  # 安装指定版本的模块
pip install --upgrade [PackageName]      # 升级某个模块
pip install [Package.whl]                # 根据本地安装文件安装
pip show [PackageName]                   # 展示已安装的某个模块的信息
pip uninstall [PackageName]              # 卸载某个模块
pip list                                 # 列出已安装的模块 
pip list --outdated                      # 查看有新版本的第三方库
pip download [PackageName]               # 下载某个模块
```

以下是常用的第三方模块
```python
pip install pillow # 图像处理标准库
pip install requests # 访问网络资源
pip install matplotlib # 数据2维可视化，作图神器
pip install numpy # 数组与矩阵运算
pip install sympy # 强大的符号计算体系完成诸如多项式求值、求极限、解方程、求积分、微分方程、级数展开、矩阵运算等等
pip install SciPy # 基于numpy 信号处理，数学、科学、工程计算功能库
pip install pandas # 数据分析高层次应用库
pip install Tensorflow # 机器学习研究，能够更快更好地将科研原型转化为生产项目
pip install pyspider # 强大的Web页面爬取系统
pip install BeautifulSoup #HTML和XML的解析库
pip install Tkinter # 可视化界面
pip install PySide # PyQt5的免费版
pip install PyQt5 # Qt开发框架的Python接口
pip install PyInstaller # 将 Python 源文件打包，通过对源文件打包， Python 程序可以在没有安装 Python 的环境中运行
pip install pipreqs #分析python文件依赖关系
```

4. 配置`PIP`安装软件资源站(清华):

直接在user目录中创建一个pip目录，如：`C:\Users\xx\pip`，新建文件`pip.ini`，内容如下

```
[global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

在安装完成基础模块之后，你可能会想

1. [安装Tensorflow开发环境](Coding/OtherLibs/Tensorflow/DevEnvDeploy.html)。
2. [安装Pytorch开发环境](Coding/OtherLibs/Pytorch/DevEnvDeploy.html)。
3. [打包你的脚本文件给一个没有安装Python环境的机器中运行](ReleasePython.html)。
