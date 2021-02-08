## Pytorch开发环境搭建

本安装包的版本搭配
* 可视化：满足[tensorboardX](https://github.com/lanpa/tensorboardX/blob/master/README.md)的要求。
* 使用Pytorch GPU的版本。
* 包含Tensorflow GPU的版本。

## 写在前面
* 要求已搭建好基本的Python环境，如果你未搭建，[点我查看如何搭建基本的Python环境](/Coding/LangsScript/Python/DevEnvDeploy.html)。
* 可视化要求搭建好`Tensorflow`环境，[点我查看如何搭建Tensorflow环境](/Coding/OtherLibs/Tensorflow/DevEnvDeploy.html)。
* 系统: Windows Enterprise 10 x64
* CPU：Intel(R) Core(TM) i7-8700 CPU @ 3.20GHz
* GPU: NVIDIA GeForce GTX 1050 Ti
* 所以本笔记记录Win10 64位系统下，TensorFlow的GPU版开发环境的搭建。

## 离线安装所需资源列表

1. `tensorflow_gpu-1.10.0-cp36-cp36m-win_amd64.whl`，会同时安装`tensorboard版本:1.10.0`；
2. `cuda_9.2.148_win10.exe`；
3. `cuda_9.2.148.1_windows.exe.exe`；
4. `pytorch-1.3.1-py3.6_cuda92_cudnn7_0.tar.bz2`;
5. `torchvision-0.4.1-py36_cu92.tar.bz2`;
6. `msgpack-0.6.2-cp36-cp36m-win_amd64.whl`.


安装步骤：

1. 在电脑任务栏，右键`NVIDIA 控制面板`>`帮助`菜单>`系统信息`>`组件`选项卡，可以看到显卡驱动支持的`CUDA`版本号为9.2。

2. 去[NVIDIA CUDA](https://developer.nvidia.com/cuda-toolkit-archive) 和[NVIDIA CUDNN](https://developer.nvidia.com/rdp/cudnn-archive) 分别下载`CUDA`和`CUDNN`相应的版本：`cuda_9.2.148_win10`和`patch`包；以及`cudnn7.2`。安装CUDA及patch包；然后将解压`Cudnn`后得到的三个小文件夹(`include`,`bin`,`lib`)复制到CUDA的安装目录(默认安装目录`C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v9.2`)即可；

3. 进入PyTorch官网，依次选择你电脑的配置
然后根据配置，去[页面](https://download.pytorch.org/whl/torch_stable.html)选择文件：找到CUDA版本为`9.2`，Python版本为`3.6`，平台为`Win64`的`1.3.1`版本的`cu92/torch-1.3.1%2Bcu92-cp36-cp36m-win_amd64.whl`文件,将其下载下来。

4. 安装: 在该whl文件所在目录打开CMD命令行，执行`pip install torch-1.3.1-cu92-cp36-cp36m-win_amd64.whl`即可。

5. 安装完成后也许会提示`msgpack`找不到，需要再额外安装一个，去[页面](https://pypi.tuna.tsinghua.edu.cn/simple下载一个msgpack-0.6.2-cp36-cp36m-win_amd64.whl)，运行`pip install msgpack-0.6.2-cp36-cp36m-win_amd64.whl`安装好即可。
去为了进行可视化，去[页面](https://pypi.tuna.tsinghua.edu.cn/packages/bb/30/6c586561c222b75c13af18beba34e1018150fff8e3cb179d91efe0d2017a/torchvision-0.4.1-cp36-cp36m-win_amd64.whl)下载后`pip install torchvision-0.4.1-cp36-cp36m-win_amd64.whl`进行安装。

## 环境测试

1. 输入python并回车，进入PYTHON环境，运行以下命令：

```python
import torch
torch.__version__    # 应该得到结果'1.4.0+cu92'
print(torch.cuda.is_available())     # 应该得到结果True
```


2. 在Visual Studio Code中，只要有Python插件，即可打开后缀名为ipynb和py的Python代码，而且可以执行Python程序。
