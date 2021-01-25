:"@echo off" : Hide the Command, Only display the result, until it comes a @echo on
:"rem" line will be displayed when @echo on
:"@rem" line will NOT be displayed when @echo on
:"echo=" print a blank line
: "@***" don't print the command itself
: "*** >nul" don't print the command'result

@echo off

call python GenMindImage.py

echo 正在复制 mermaid.min.js 文件...

@xcopy /y .\mds\SoftTuto\Manage\Git\res\mermaid.min.js .\mds\node_modules\mermaid\dist >nul
@xcopy /y .\mds\SoftTuto\Manage\Git\res\mermaid.min.js .\mds\node_modules\gitbook-plugin-mermaid-gb3\dist\mermaid >nul
echo=
echo 复制 mermaid.min.js 文件完成!
echo=
echo 正在编译你的 Gitbook ...
echo=
@call gitbook build ./mds/. ./docs
echo=
echo 编译你的 Gitbook 完成!

echo=
echo 正在做最后处理,请耐心等候...
@xcopy /y .\mds\SoftTuto\Manage\Git\res\theme.js .\docs\gitbook >nul

echo=
echo 完成！ 


for /f "tokens=3,4" %%a in ('"reg query HKEY_CLASSES_ROOT\http\shell\open\command"') do (set SoftWareRoot=%%a %%b)
start "" % SoftWareRoot % "%cd%\docs\index.html"

echo=
echo 请查阅你的浏览器,尽情享阅吧~
echo=
pause