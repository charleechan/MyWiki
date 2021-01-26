# 本Wiki维护教程




1. 在<mark>已有分类</mark>的路径下添加markdown文件,需满足以下要求;
   * 请把文件名设置为 **英文开头，且只有英文和数字, 后缀名为.md**;
   * 文件内容的**第一个非空行将作为内容索引**, 因此:
     * 第一个非空行中<mark>禁止链接和行内代码</mark>.
     * 第一个非空行最好是中文名。
2. 如果要<mark>新建分类</mark>,需要修改`GenSideBarNav.py`和`GenMindImage.py`脚本中的`main()`函数.
3. 运行脚本`GitbookBuild.bat`,本脚本将自动:
   * 运行根目录的`GenMindImage.py`脚本, 将为每个子分类建立目录页(README.md)
   * 运行根目录的`GenSideBarNav.py`脚本, 将更新`mds`目录下的`SUMMARY.md`文件，以建立侧边栏目录。
   * 自动编译生成Gitbook的网页文件(./docs).
   * 自动打开浏览器预览本地电子书.

> <mark>警告</mark>: 使用脚本`GitbookResetReadMe.bat`会将**所有分类的目录页置为404页面**.

**本站通过脚本自动生成目录(导航)页,但前提是有本地已经安装了**<mark>Python</mark>. 

* 如果还没安装,需要把[pythonlib.zip](https://github.com/cherleechan/MyWiki/pythonlib.zip) 放在与脚本同一目录,并解压到当前文件夹.并修改`GitbookBuild.bat`的10~13行.

```
MyWiki
  |--docs : gitbook build生成的网页,xxx.github.io从本文件夹读取生成Pages.
  |--mds
  |   |--README.md
  |	  |--SUMMARY.md
  |   |--node_modules
  |   |--Coding
  |   |--SoftTuto
  |   |--img : 包含网页logo.
  |
  |--pythonlib : 
  |   |--python.exe
  |   |...
  |
  |--GitbookBuild.bat : 一键生成导航页的脚本,会使用脚本 GenMindImage.py 和 GenSideBarNav.py
  |--GenMindImage.py, GenSideBarNav.py : python脚本,不可删除.
  |--GitbookResetReadMe.bat : 一键置404,用处不大.

```

