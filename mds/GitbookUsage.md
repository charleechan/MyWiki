# 结合Github Pages使用GitBook

> [参考](https://www.jianshu.com/p/3d03ab330df5)

## 概述
GitBook 是一个 Node.js 环境下，用于构建电子书的工具。

GitBook 让你能够使用 Markdown 来编排一本电子书，GitBook 能够根据 Markdown 文档，生成 PDF、ePub 或 Mobi 文档，还可以生成静态网页。

你可以将 GitBook 生成的静态资源放到某个静态网站的托管平台上（如 GitHub Pages），以便他人可以在线阅读你创作的内容。

GitBook 工作在 Node.js 环境下，因此，你需要确保你已经配置好 Node.js 环境。

## 安装Node.js

1. 下载node.js并安装（可能操作不对，.zip结尾的不知道怎么的不好用，我用的.msi结尾的正常）

2. 测试下是否安装完成, 安装完成后，点击`node.exe`，输入：`console.log("Hello,World!");` 回车能正常显示`hello，world`就OK

3. 在cmd中设置node.js的文件夹
```
npm config set prefix "D:\Program\nodejs\node_modules\node_global"
npm config set cache "D:\Program\nodejs\node_modules\node_cache"
```

4. 新增用户环境变量`NODE_PATH`,值为`D:\Program\nodejs\node_global\node_modules`;

5. 设置用户环境变量`PATH`,把其中node的路径值改成`D:\Program\nodejs\node_modules\node_global`

## 安装 gitbook-cli


1. 通过cmd调用窗口，进入安装nodeJs的目录，输入命令全局安装gitbook：`npm install gitbook-cli -g`

2. 输入命令：`mkdir MyWiki`，创建文件夹


3. 执行下面命令，查看 `gitbook-cli` 的版本，以确定其是否成功安装。
    ```
    $ gitbook -V
    CLI version: 2.3.2
    gitbook version: 3.2.3
    ```
4. 可能会报错`if (cb) cb.apply(this, arguments)`,　打开`polyfills.js`文件，在第62-64行调用了这个函数,因此把62-64行注释掉.
5. 4不报错也注释掉.
	
## 开始

在CMD中找到你要新建gitbook的位置,执行下面命令，gitbook 将完成一些准备工作。
```bash
gitbook init
```
实际上，上面命令生成了下面 2 个文件。

├── README.md
└── SUMMARY.md

README.md 将包含电子书的简介

SUMMARY.md 将包含电子书的目录

有了这两个文件，就是一本结构完整的电子书了。

## 编辑电子书内容
初始化后的目录中会出现`README.md（电子书简介文件）`和`SUMMARY.md（导航目录文件）`两个基本文件。除此之外还可以手动新建其它`Glossary.md（书尾的词汇表）`、`book.json（电子书配置文件）`。

电子书的正文内容可以根据自己的喜好创建新的后缀为 .md 文件，如“chapter01.md”，然后用 `MarkDown` 编写具体的文本内容即可。下面对这些文件分别做详细介绍。

1. README.md
此文件是简单的电子书介绍，可以把您所制作的电子书做一下简单的描述：

```
# 简介

这是我的第一本使用 GitBook 制作的电子书。
```

2. SUMMARY.md
此为电子书的导航目录文件，每当新增一个章节文件就需要向此文件中添加一条记录。对于 Kindle 电子书来说，此文件所呈现的目录结构就是开头的目录内容和“前往”的目录导航。

```
# Summary

* [简介](README.md)
* [第一章](section1/README.md)
* [第二章](section2/README.md)
```

如果需要“子章节”可以使用 Tab 缩进来实现（最多支持三级标题），如下所示：

```
# Summary

* [第一章](section1/README.md)
    * [第一节](section1/example1.md)
    * [第二节](section1/example2.md)
* [第二章](section2/README.md)
    * [第一节](section2/example1.md)
```

3. Glossary.md
对于电子书内容中需要解释的词汇可在此文件中定义。词汇表会被放在电子书末尾。其格式如下所示：

```
# 电子书
电子书是指将文字、图片、声音、影像等讯息内容数字化的出版物和植入或下载数字化文字、图片、声音、影像等讯息内容的集存储和显示终端于一体的手持阅读器。

# Kindle
Amazon Kindle 是由 Amazon 设计和销售的电子书阅读器（以及软件平台）。用户可以通过无线网络使用 Amazon Kindle 购买、下载和阅读电子书、报纸、杂志、博客及其他电子媒体。
```

4. book.json


“book.json”是电子书的配置文件，可以看作是电子书的`原数据`，比如 title、description、isbn、language、direction、styles 等，更多点击这里查看。它的基本结构如下所示：

```json
{
    "title": "我的第一本電子書",
    "description": "用 GitBook 制作的第一本電子書！",
    "isbn": "978-3-16-148410-0",
    "language": "zh-tw",
    "direction": "ltr"
}
```

5. `普通章节.md` 文件

`普通章节.md` 文件可以使用您感觉顺手的文本编辑器编写。MarkDown 的写法可以点击这里查看相关示例。每编写一个 .md 文件，不要忘了在`SUMMARY.md`文件中添加一条记录哦。

6. 电子书封面图片

GitBook 帮助文档建议封面图片的尺寸为 `1800*2360` 像素并且遵循建议：

* 没有边框
* 清晰可见的书本标题
* 任何重要的文字在小版本中应该可见
* 图片的格式为 jpg 格式。把图片重命名为`cover.jpg`放到电子书项目文件夹即可。

## 预览
执行`gitbook serve`,用浏览器打开 `http://localhost:4000`，就可以看到电子书的最终效果了。

## 生成

执行下面命令，就可以将电子书的内容制作成静态网页，并保存在 `_book` 目录中。

```bash
gitbook build
```

## 导出为其他电子书文件
确定电子书没有问题后，可以通过输入以下命令生成 `mobi` 电子书：

```bash
gitbook mobi ./ ./MyFirstBook.mobi
```

如果出现以下错误提示，说明您还未安装 Calibre。由于 GitBook 生成 mobi 格式电子书依赖 `Calibre` 的 `ebook-convert`，所以请先点击这里下载安装 Calibre。

```bash
Error: Need to install ebook-convert from Calibre
```

Calibre 安装完毕后，对于 Mac OS X 系统，还需要先设置一下软链接：

```bash
ln -s /Applications/calibre.app/Contents/MacOS/ebook-convert /usr/local/bin
```

再次运行转换命令，即可生成 mobi 格式电子书。




## 结合 GitHub Pages
GitHub Pages 是 GitHub 提供的静态网站托管服务。

GitHub 上的每个仓库都可以拥有一个 GitHub Pages，对应的 URL 如下：`https://<username>.github.io/<repository>/`

GitHub Pages 的静态资源支持下面 3 个来源：

* master 分支
* master 分支的 /docs 目录
* gh-pages 分支
执行下面命令，在生成静态网页时，将保存的目录指定为 `./docs`

```bash
# 把mds目录下的所有文件编译成为电子书, 输出目录为docs
gitbook build ./mds/. ./docs
```

然后直接推送到 GitHub 仓库。

```bash
git push origin master
```

最后选择仓库的`setting`,`Pages`,选择分支`main`-`docs`作为主目录,就可以在`[username].github.io/[repository name]`看到书啦.
> 将 `_book` 目录推送到 `GitHub` 仓库的 `gh-pages` 分支:`$ git subtree push --prefix=_book origin gh-pages`也可以。

## 更进一步: 使用Gitbook插件定制化页面

GitBook使用[基于Node.Js的Gitbook插件](https://www.npmjs.com/)对Markdown文件进行渲染.


1. 写配置文件:在根目录新建`book.json`,在`book.json`中写入以下代码:
```json
{
    "plugins": [
        "wavedrom",
        "back-to-top-button",
        "chapter-fold",
        "splitter",
        "code",
        "-lunr",
        "-search",
        "-sharing",
        "sharing-plus",
        "search-pro",
        "insert-logo",
        "custom-favicon",
        "pageview-count",
        "tbfed-pagefooter",
        "mind-maps",
        "hide-element",
        "mathjax",
        "forkmegithub",
        "mermaid-gb3"
    ],
    "pluginsConfig": {
        "insert-logo": {
            "url": "./img/logo.png",
            "style": "background: none; max-height: 30px; min-height: 30px"
        },
        "favicon": "./img/inlook.ico",
        "tbfed-pagefooter": {
            "copyright": "Copyright &copy charleechan 2021",
            "modify_label": "本文最终修订于：",
            "modify_format": "YYYY-MM-DD HH:mm:ss"
        },
        "forkmegithub": {
          "url": "https://github.com/your/repo"
        },
        "sharing": {
            "douban": true,
            "facebook": false,
            "google": false,
            "hatenaBookmark": false,
            "instapaper": false,
            "line": false,
            "linkedin": false,
            "messenger": false,
            "pocket": false,
            "qq": true,
            "qzone": false,
            "stumbleupon": false,
            "twitter": true,
            "viber": false,
            "vk": false,
            "weibo": true,
            "whatsapp": false,
            "all": [
                "facebook", "google", "twitter",
                "weibo", "instapaper", "linkedin",
                "pocket", "stumbleupon"
            ]
        },
        "hide-element": {
            "elements": [".gitbook-link"]
        }
    }
}
```
其中

```bash
# disable 掉Gitbook内置的搜索功能的后台
-lunr
# disable 掉Gitbook内置的搜索功能的部件
-search
# disable 掉Gitbook内置的分享功能的部件
-sharing
# wavedrom 插件, 渲染代码块wavedrom为时序图或电路图
wavedrom
# 返回顶部按钮
back-to-top-button
# 导航目录折叠
chapter-fold
# 侧边栏宽度可调节
splitter
# 给代码块增加复制代码按钮和行号
code-pro
# 分享功能增强
sharing-plus
# 高级搜索,支持中英文,准确率更高
search-pro
# 个性化网站导航栏的logo
insert-logo
# 个性化网站的icon
custom-favicon
# 个性化文章的页脚, 增加版权和修改时间
tbfed-pagefooter
# 文档页面阅读数
pageview-count
# 思维导图
mind-maps
# 隐藏元素
hide-element
# 支持mathjax公式
mathjax
# 支持mermaid画图
mermaid
# 右上角添加fork me 丝带
forkmegithub-cn
```

3. 执行命令`gitbook install`,将自动安装gitbook插件,然后使用gitbook 编译即可.

4. 如果编译中`mathjax`出现错误,使用以下命令将mathjax包降级,`npm install mathjax@2.7.6`