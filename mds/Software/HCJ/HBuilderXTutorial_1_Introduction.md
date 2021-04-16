# HBuilderX 1-引言
> 要做一款安卓APP,咱们得先学安卓开发语言,例如java,前端后端。那么没有这些开发语言基础,咱们怎么做呢？其实现在有比较好的开发方案就是做webAPP,咱们可以用web前端知识构建安卓客户端,用php构建服务端。

**html+css+js+Hbuilder开发一款安卓APP,根本不用学Android开发！**

<mark>html负责页面内容,js负责效果以及调用原生app方法,ui框架负责样式!</mark>
<mark>html负责页面内容,js负责效果以及调用原生app方法,ui框架负责样式!</mark>
<mark>html负责页面内容,js负责效果以及调用原生app方法,ui框架负责样式!</mark>

`HBuilderX`可以将`html`+`js`+`ui`打包成`apk`或者`ipa`,制作安卓/苹果安装包.

类似的`Electron`可以将`html`+`js`+`ui`打包成`exe`,在桌面运行.

## 预备知识
1. html+css+js基础知识,这是web前端开发最基础的
2. php后端,mysql数据库基础知识
3. HbuilderX,这是一款IDE,集成代码编辑器,运行,真机模拟,调试等工具,还支持在线打包,也就是说你不用配置什么java开发环境就可以开发安卓软件,[戳这里下载软件](https://www.dcloud.io/)
4. 前端UI框架,本次教程我使用的是谷歌的MDUI框架,[请戳这里下载](https://www.mdui.org/)

> 当然,如果学习能力强,以上都不是问题.你可以直接下手搞!

## 开始HBuilderX之旅

1. 先打开HbuilderX（以下简称HB）
2. 创建一个`webapp`工程(也就是`移动App`),空模板就行;
3. 可以创建在桌面,然后就可以看到整个工程的目录了,但系统默认生成的文件,可以删掉,留下一个`manifest.json`;
4. 然后把我们提前下载好的前端UI所有文件`Copy`进来,我用的是`MDUI`;
5. 将此文件夹压缩成zip,方便以后使用,解压就可以用;
6. 如果需要JRE(Java Runtime Environment)环境,自己安装后添加PATH变量即可;
7. 打开HBuilder之后默认会有一个项目"HelloHBuilder",里面有HBuilder使用的介绍;
8. 