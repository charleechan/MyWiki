# 本Wiki维护教程

1. 在相应分类的路径下添加markdown文件;
2. 维护`mds`目录下的`SUMMARY.md`文件，建立侧边栏目录。
3. 运行脚本`GitbookBuild.bat`,将自动
   * 运行根目录的`GenMindImage.py`脚本,将为每个子分类建立目录页(README.md)
   * 编译生成Gitbook的网页文件(./docs).
   * 自动打开浏览器预览本地电纸书.

> <mark>警告</mark>: 使用脚本`ResetReadMe.bat`会将**所有分类的目录页置为404页面**.