:"@echo off" : Hide the Command, Only display the result, until it comes a @echo on
:"rem" line will be displayed when @echo on
:"@rem" line will NOT be displayed when @echo on
:"echo=" print a blank line
: "@***" don't print the command itself
: "*** >nul" don't print the command'result

@echo off

call python GenMindImage.py

echo ���ڸ��� mermaid.min.js �ļ�...

@xcopy /y .\mds\SoftTuto\Manage\Git\res\mermaid.min.js .\mds\node_modules\mermaid\dist >nul
@xcopy /y .\mds\SoftTuto\Manage\Git\res\mermaid.min.js .\mds\node_modules\gitbook-plugin-mermaid-gb3\dist\mermaid >nul
echo=
echo ���� mermaid.min.js �ļ����!
echo=
echo ���ڱ������ Gitbook ...
echo=
@call gitbook build ./mds/. ./docs
echo=
echo ������� Gitbook ���!

echo=
echo �����������,�����ĵȺ�...
@xcopy /y .\mds\SoftTuto\Manage\Git\res\theme.js .\docs\gitbook >nul

echo=
echo ��ɣ� 


for /f "tokens=3,4" %%a in ('"reg query HKEY_CLASSES_ROOT\http\shell\open\command"') do (set SoftWareRoot=%%a %%b)
start "" % SoftWareRoot % "%cd%\docs\index.html"

echo=
echo �������������,�������İ�~
echo=
pause