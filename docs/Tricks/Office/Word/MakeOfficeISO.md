# Office 2019的ISO制作,安装,与激活

## 缘起 

事情的起因是这样的~

用VISIO画图，发现形状不能检索，搜索后啥也没有~

上网查询一通后发现，怀疑是语言问题~

果断卸载Office 2019 专业增强中文版，安装相应的英文版~

然后就可以用Visio 形状搜索了~

然鹅，有时候我还想用中文版office怎么办...

微软给了办法是下载 OFFICE显示语言包，[中文版的网站](https://support.microsoft.com/zh-cn/topic/office-%E8%AF%AD%E8%A8%80%E9%99%84%E4%BB%B6%E5%8C%85-82ee1236-0f9a-45ee-9c72-05b026ee809f) 下载不了，用[英文版网站](https://support.microsoft.com/en-us/topic/language-accessory-pack-for-office-82ee1236-0f9a-45ee-9c72-05b026ee809f) 才可以下载该语言包。。

于是下载，双击，发现微软开始疯狂下载语言包~~

那么问题来了，内网计算机也这么搞吗~我要离线安装包！！

搜索一通，仍然没找到...于是萌生出一个想法: Office 中文+英文 的ISO。

## 步骤1-下载 Office tool plus

去 `Office Tool Plus`[官网](https://otp.landian.vip/zh-cn/download.html)下载最新的`Office Tool Plus`，解压之后，您应该能看见 Runtime 文件夹和 setup 文件。

打开Office Tool Plus.exe，点击部署。

## 步骤2-下载Office 安装文件

**下载 Office 安装文件与当前电脑上的 Office 无关，因此不需要考虑电脑上已安装的 Office。**

下载 Office 安装文件前，需要确定5个内容：

* 体系结构：这里选择`64位`。
  * 体系结构有 32 位和 64 位可以选择，通常情况下，我们只需要创建一个版本的即可。
  * 如果需要分别创建 32 位和 64 位版本的，请先创建一个版本，然后删除现有的 Office 安装文件，再下载并创建另一个版本的。
  * 如果需要创建 32 位和 64 位合集版本，请先下载一个版本，再下载另一个版本。重复的文件会自动跳过，不会重复下载。
* 通道：这里选择`Office 2019 企业长期版`
  * 正常情况下，选择“当前通道”、“半年度企业版通道”中的一个即可，其它通道按需选择。
* 部署模式：这里选择`仅下载`
  * 为了能下载 Office ISO 文件，请务必将部署模式更改为“仅下载”。
* 安装模块：这里选择`Office部署工具`
  * 选择要使用的部署工具。
* 产品和语言：
  * 在左侧添加你所需要的产品和语言，如果你不添加语言，则使用 Office ISO 进行安装时仍然需要下载语言包。
  * 产品选择： `Office 专业增强版2019-批量版`+`Visio专业版2019-批量版`
    * 下面的组件根据需要，这里只选择了`word`,`excel`,`powerpoint`。
  * 语言选择：`简体中文(中国)`+`English(United States)`

配置完以上信息后，若 Office Tool Plus 没有提示任何错误信息，点击开始部署，即可下载 Office 安装文件。

## 步骤3-是否按配置文件自动安装

如果保存当前配置，那么在步骤5中，打开ISO中的`Office Tool Plus`时，会按配置文件自动安装已选的程序，如Word,Visio等。

如果你不需要自动安装，**按下 F5 清空当前配置**。

**那么如何保存当前配置?**

当前的配置信息可以通过点击`查看 XML 代码`了解，然后点击下拉菜单，点`导出配置`，可以看到保存了一个configure.xml文件。

为了让用户选择自己需要的组件，这里选择不自动安装，**按下 F5 清空当前配置**。


## 步骤4-创建 Office ISO 文件

将部署模式从`仅下载`更改为`创建 ISO 文件`，然后点击`开始部署`，Office Tool Plus 将会提示你选择文件保存位置，这里命名为`Office_2019_ProPlus_EN_CN_*****.iso`，之后 `Office Tool Plus` 将会制作 Office ISO 文件并储存。

创建完成之后，您应该验证此 Office ISO 是否可以正常工作。

## 步骤5-安装Office 专业增强 中文+英文版本

首先卸载目标机器已有的Office。

将刚刚生成的`Office ISO` 文件拷贝到目标机器上；

双击进行挂载；

双击打开虚拟光驱中的`Office Tool Plus.exe`：

点是：将会按配置文件自动安装已选的组件，包括`word`,`excel`,`powerpoint`,`Visio`。

点否：可以自己增加选择其他组件。


## 步骤6-激活Office

* 自动激活
  1. 清除激活信息，为了避免出现激活信息不正确的问题，请在激活 Office 之前清除旧的 Office 激活信息（如果有）。
  2. 一键激活: Office，Visio，Project等：按下键盘上的 Ctrl + P，Office Tool Plus 将会在顶栏显示一个命令输入框，按需复制下面的命令，粘贴后回车以执行操作。
  `/osppilbyid MondoVolume /osppsethst:kms.loli.beer /osppsetprt:1688 /osppact`

* 手动激活

  * 许可证管理：安装一个 `Office 专业增强版2019-批量版-[ProPlus2019Volume]`许可证，以及`Visio 专业版 2019-批量版-[VisioPro2019Volume]`，静静等待许可证安装完成。
  * 设置一个 KMS 地址（可以设置端口为 1688）（KMS 地址在下面有列表）。

  ```
  kms.loli.beer
  kms.loli.best
  kms.cangshui.net
  kms.iaini.net
  kms.ddz.red
  kms.ghpym.com
  kms.qkeke.com
  kms.wxlost.com
  kms.heng07.com
  kms8.MSGuides.com
  kms.kuretru.com
  kms.moeclub.org
  cy2617.jios.org
  kms.bige0.com
  kms.jm33.me
  kms.zhuxiaole.org
  windows.kms.app
  nb.shenqw.win
  kms.magicwall.org
  
  下列地址因出现问题或不稳定而不推荐使用：
  
  kms.mogeko.me (不稳定)
  kms.03k.org (不稳定)
  kms2.loli.best
  kms.ddddg.cn
  kms.ijio.net
  home.aalook.com
  zh.us.to
  k.zpale.com
  ```
* 点击激活按钮，等待激活完成。

## 步骤7-增删应用程序（例如 Access，PowerPoint）

在部署页面的应用程序卡片中，将自己想要的应用程序打勾，不想要的取消打勾，

然后点击开始部署，即可增加/卸载指定的应用程序。

如果您想添加一个 Access，但是发现应用程序里面没有 Access 可以选？

添加一个产品，选择 Access 即可，可以选择 Access 2019/2016 - 批量版，好激活。

## 步骤8-增删一个或多个产品（语言包同理）

Office Tool Plus 中可以在已安装 Office 的情况下增加一个或者多个产品，

添加完成后，直接开始部署即可。

在系统自带的程序管理中，我们可以一次性卸载单个产品。

如果要一次性删除多个产品，在部署页面点击产品/语言的卸载，然后开始部署即可。