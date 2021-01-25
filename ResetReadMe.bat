:"@echo off" : Hide the Command, Only display the result, until it comes a @echo on
:"rem" line will be displayed when @echo on
:"@rem" line will NOT be displayed when @echo on
:"echo=" print a blank line
: "@***" don't print the command itself
: "call ***.bat " don't print the command itself
: "*** >nul" don't print the command'result

@echo off

echo 本脚本功能: 将所有readme.md 替换为默认的404页面.

echo 正在批量复制 Default.md 文件...

@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsConf\Json\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsGene\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsGene\C\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsGene\Cpp\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsGene\Java\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsHard\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsHard\SystemVerilog\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsHard\Verilog\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsHard\VHDL\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsMark\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsMark\HTML\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsMark\MD\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsMark\QML\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsMark\XML\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\Bash\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\CMD\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\JS\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\Matlab\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\PHP\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\Python\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\SQL\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsScript\TCL\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsStyle\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\Coding\LangsStyle\CSS\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Animation\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Animation\HTML5\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Animation\PocketAnimation\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Animation\SolidWorks\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\GIMP\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\Mermaid\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\Origin\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\Solidworks\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Image\Visio\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Manage\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Manage\Git\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Manage\Inlook\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Manage\Outlook\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Office\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Office\Excel\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Office\PPT\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Office\Word\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\ChromeExt\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\GIMPPlu\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\GitbookPlu\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\OfficePlu\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Plugins\VSCodeExt\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\AltiumDesigner\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\CadenceSPB\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\KeilMDK\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\ModelSim\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\MultiSim\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\Qt\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\SolidWorks\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\VisualStudio\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\Vivado\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\VSCode\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Video\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Video\VideoStudio\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\OtherLibs\OpenCV\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\OtherLibs\Pytorch\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\OtherLibs\Tensorflow\README.md >nul
@xcopy /y .\mds\res\Default.md .\mds\SoftTuto\Project\Others\README.md >nul

echo=
echo 已完成~

pause