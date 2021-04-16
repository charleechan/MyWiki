# Tensorflow开发环境搭建

本教程将包含Tensorflow GPU的版本的安装过程。

## 写在前面
* 要求已搭建好基本的Python环境，如果你未搭建，[点我查看如何搭建基本的Python环境](/Coding/LangsScript/Python/DevEnvDeploy.html)。
* 系统: Windows Enterprise 10 x64
* CPU：Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz
* GPU: NVIDIA GeForce GTX 1050 Ti
* 所以本笔记记录Win10 64位系统下，TensorFlow的GPU版开发环境的搭建。

## 离线安装所需文件

1. `tensorflow_gpu-1.10.0-cp36-cp36m-win_amd64.whl`；
2. `cuda_9.2.148_win10.exe`；
3. `cuda_9.2.148.1_windows.exe.exe`；
4. `cudnn-9.2-windows10-x64-v7.2.1.38.zip`；

## 安装步骤

1. 在电脑任务栏，右键`NVIDIA 控制面板`>`帮助`菜单>`系统信息`>`组件`选项卡，可以看到显卡驱动支持的`CUDA`版本号为9.2。

2. 去[Github](https://github.com/fo40225/tensorflow-windows-wheel)下载一个你想下载的tensorflow的版本，这里分别依次选择`tensorflow-windows-wheel/1.10.0/py36/GPU/`，
下载`cuda92cudnn72avx2`文件夹下的`*.whl`文件，我下载的是`tensorflow_gpu-1.10.0-cp36-cp36m-win_amd64.whl`，可以看到这里的文件名给出了配置要求：`cuda 9.2`版本，`cudnn`要求7.2版本，记下这两个版本号。

3. 去[NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit-archive) 和[NVIDIA CUDNN](https://developer.nvidia.com/rdp/cudnn-archive) 分别下载`CUDA`和`CUDNN`相应的版本：`cuda_9.2.148_win10`和`patch`包；以及`cudnn7.2`。安装CUDA及patch包；然后将解压`Cudnn`后得到的三个小文件夹(`include`,`bin`,`lib`)复制到CUDA的安装目录(默认安装目录`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.2`)即可；

4. 进入你`.whl`文件所在的目录，输入`pip install tensorflow_gpu-1.10.0-cp36-cp36m-win_amd64.whl`即可安装

5. 在当前环境下输入python进入python编辑环境，输入以下代码进行测试

```python
import tensorflow as tf
hello = tf.constant("Hello, Tensorflow!")
sess = tf.Session()
print(sess.run(hello))

a=tf.constant(10)
b = tf.constant(20)
print(sess.run(a+b))
```

## 测试环境

1. 对tensorflow说Hello!

 ```python
 import tensorflow as tf
 hello = tf.constant("Hello, Tensorflow!")
 sess = tf.Session()
 print(sess.run(hello))
 ```

2. 进一步测试：

 首先看看tensorflow是不是正常安装并可以导入了：

  **测试代码一：**
```
import tensorflow as tf
a = tf.test.is_built_with_cuda()  # 判断CUDA是否可以用
b = tf.test.is_gpu_available(
cuda_only=False,
min_cuda_compute_capability=None
)  # 判断GPU是否可以用
print(a)
print(b)
```

 输出结果是：
```python
True
True
```
 代表CUDA和GPU可用

 **测试代码二：**
 
 ```
 import tensorflow as tf
 #Creates a graph.
 
 a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
 b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
 c = tf.matmul(a, b)
 
 #Creates a session with log_device_placement set to True.
 sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
 
 #Runs the op.
 print(sess.run(c))
 ```

 输出结果是：

 ```
 [[22. 28.] [49. 64.]]
 ```

3. 利用GPU测试TensorFlow的运行情况

 下面是直观的看出代码有没有在使用GPU

 **测试代码三：**

 ```
 import tensorflow as tf
 with tf.device('/cpu:0'):
   a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
   b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
 with tf.device('/gpu:1'):
  c = a + b
 sess =tf.Session(config=tf.ConfigProto(log_device_placement=True))
 sess.run(tf.global_variables_initializer())
 print(sess.run(c))
 ```

**注意**：

1. 上述测试代码三中可能报错，你需要更改代码为

    `sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))`

  其中

 * `allow_soft_placement=True` 表明：计算设备可自行选择，如果没有这个参数，会报错。因为不是所有的操作都可以被放在GPU上，如果强行将无法放在GPU上的操作指定到GPU上，将会报错。

 * `log_device_placement=True` 表明：计算设备的日志log文件会实时显示(使用Python命令行时会显示，使用spyder时不显示,使用spyder可以使用性能分析工具进行查看)。

 先不急着运行，打开任务管理器，点击  性能  ，找到你自己英伟达显卡的GPU那一栏，点击一下，可以显示GPU的利用情况，正常情况下你没运行什么程序，GPU利用率什么的都是0，没有波澜，然后你运行代码三，会发现GPU利用率开始变化了。

## 更进一步

* 上面已经完全测试了windows10系统下tensorflow-gpu的开发环境。如果你想了解的更多一点：可以尝试学习一下这段代码:

```python
import tensorflow as tf
import numpy as np

# 1 collect data
x_data = np.float32(np.random.rand(200,2));
y_data = np.matmul(x_data,[[5.2],[9.6]])+3.4;

# 2 Ceate model
W = tf.Variable(tf.random_uniform([2,1],-1,1));
b = tf.Variable(tf.zeros([1]));
y_ = tf.matmul(x_data,W)+b;

# 3 loss function
loss = tf.reduce_mean(tf.square(y_-y_data));
optimizer = tf.train.GradientDescentOptimizer(0.5);
train = optimizer.minimize(loss);

# 4 Initialzer
init = tf.initialize_all_variables();
sess = tf.Session(config = tf.ConfigProto(allow_soft_placement=True,log_device_placement=True));
sess.run(init);

# 5 Train
for step in range(0,201):
    sess.run(train);
    if step%10 == 0:
        print(step,np.transpose(sess.run(W)),sess.run(b));

# 6 Output
sess.close();
```

## 使用Visual Studio Code进行开发

使用Visual Studio Code也可以进行python的开发。你需要安装`Python`插件。即可编写代码。编写完成后按`F1`或`Ctrl+Shift+P`，调出命令框，输入`python: select interpreter`来选择解释器，点击之后可以选择你的conda的tensorflow环境下的解释器。在状态栏就可以看到"Python 3.6.8 64-bit"字样，表示当前的运行环境。此时按`Ctrl + F5`运行代码，按`F5`进行调试。

开心玩耍吧~

个人使用体验：VS Code比Pycharm还要流畅一些~~


## 写在最后
为保证以后该环境不出幺蛾子，

**请不要更改GPU驱动**

**请不要更新GPU驱动**

**请不要更新GPU驱动**

**如果你不慎更新了显卡驱动，按此笔记重新安装配置环境。**