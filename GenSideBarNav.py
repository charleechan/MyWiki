# -*- using: utf-8 -*-

import os
import sys
# 本文件功能: 一键生成侧边栏导航
def recu_list_subdirs(path,summaryFileDir,sumFile,libDict,indent=0):
    # 列出某目录下的文件
    for item in os.listdir(path):  
        # 获得子项路径     
        curPath = os.path.join(path, item)
        # 如果是个文件夹,且包括README.md
        if os.path.isdir(curPath):
            curRDFile = curPath+"\\README.md"
            if os.path.exists(curRDFile):
                trimPath=curPath.replace(summaryFileDir,"")
                if libDict.__contains__(trimPath):
                    dstStr = trimPath.replace("\\","/")+"/README.md"
                    dstStr = dstStr.lstrip("/")
                    dstStr = ' ' * indent + '* [' + libDict[trimPath] + "]("+dstStr+")\n"
                    sumFile.write(dstStr)
                recu_list_subdirs(curPath,summaryFileDir,sumFile,libDict,indent + 2)
        # 如果是个文件
        if os.path.isfile(curPath):
            file_name,ext_name = os.path.splitext(item)
            if (not item=="README.md") and (ext_name==".md"):


                trimPath=curPath.replace(summaryFileDir,"")
                trimPath = trimPath.replace("\\","/")
                trimPath = trimPath.lstrip("/")
                
                titleStr = ""
                with open(curPath,mode="r",encoding="utf_8") as f:
                    for line_number, line in enumerate(f, 1):
                        if (not line.isspace()):
                            line = line.lstrip("#")
                            line = line.lstrip(" ")
                            line = line.rstrip(":")
                            line = line.rstrip("：")
                            titleStr = line
                            break
                titleStr = titleStr.rstrip("\n")
                dstStr = ' ' * indent + '* [' + titleStr + "](" +trimPath+ ")"
                # print(dstStr)
                sumFile.write(dstStr+"\n")



def createNavPage(summaryFileDir,libDict,libList):
    filepath = __file__
    realpath = os.path.realpath(filepath)
    current_path = os.path.dirname(realpath)
    summaryFileDir = current_path + summaryFileDir
    summaryFile = summaryFileDir +"\\SUMMARY.md"
    
    with open(summaryFile,mode="w",encoding="utf_8") as sumFile:
        sumFile.write("# Summary\n\n## 知识体系\n* [我的Wiki-一本正经地胡说八道](README.md)\n* [我的Wiki-编程平台](nav1.md)\n* [我的Wiki-软件教程](nav2.md)\n")
        for libdir in libList:
            cur_path = summaryFileDir + libdir
            if(libDict.__contains__(libdir)):
                sumFile.write("\n## "+libDict[libdir]+"\n")
            recu_list_subdirs(cur_path,summaryFileDir,sumFile,libDict)




def main():

    libDict={}
    # 如果您已增加各级文件夹,请在下面添加相应的路径,以及侧边栏导航名字
    
    libList = []
    # 在vvvv下面vvvv添加一级文件夹vvvvvvv
    libList.append('\\Coding')
    libList.append('\\SoftTuto')
    libList.append('\\KnowWorld')
    # 在^^^^上面^^^^添加一级文件夹^^^^^^^
    
    
    # 在vvvv下面vvvv添加各级文件夹vvvvvvv
    # libDict[文件夹的路径]                ="侧边栏导航名字"
    
    libDict["\\Coding"]                    ="编程语言"

    libDict["\\Coding\\LangsGene"]         ="通用编程语言"
    libDict["\\Coding\\LangsGene\\C"]      ="C语言"
    libDict["\\Coding\\LangsGene\\Cpp"]    ="C++"
    libDict["\\Coding\\LangsGene\\Java"]   ="Java"

    libDict["\\Coding\\LangsHard"]             ="硬件描述语言"
    libDict["\\Coding\\LangsHard\\Verilog"]    ="Verilog HDL"
    libDict["\\Coding\\LangsHard\\VHDL"]       ="VHDL"
    libDict["\\Coding\\LangsHard\\SV"]         ="System Verilog"

    libDict["\\Coding\\LangsMark"]         ="标记语言"
    libDict["\\Coding\\LangsMark\\MD"]     ="Markdown"
    libDict["\\Coding\\LangsMark\\HTML"]   ="HTML"
    libDict["\\Coding\\LangsMark\\QML"]    ="QML"
    libDict["\\Coding\\LangsMark\\XML"]    ="XML"

    libDict["\\Coding\\LangsScript"]         ="脚本"
    libDict["\\Coding\\LangsScript\\JS"]     ="Javascript/QScript"
    libDict["\\Coding\\LangsScript\\Bash"]   ="Bash"
    libDict["\\Coding\\LangsScript\\CMD"]    ="CMD 命令行"
    libDict["\\Coding\\LangsScript\\Matlab"] ="Matlab"
    libDict["\\Coding\\LangsScript\\Python"] ="Python"
    libDict["\\Coding\\LangsScript\\SQL"]    ="SQL"
    libDict["\\Coding\\LangsScript\\TCL"]    ="TCL"
    libDict["\\Coding\\LangsScript\\PHP"]    ="PHP"

    libDict["\\Coding\\OtherLibs"]             ="库/框架"
    libDict["\\Coding\\OtherLibs\\Tensorflow"] ="Tensorflow"
    libDict["\\Coding\\OtherLibs\\Pytorch"]    ="Pytorch"
    libDict["\\Coding\\OtherLibs\\OpenCV"]     ="OpenCV"

    libDict["\\Coding\\LangsStyle"]          ="样式表"
    libDict["\\Coding\\LangsStyle\\CSS"]     ="CSS/QSS"

    libDict["\\Coding\\LangsConf"]         ="配置文件"
    libDict["\\Coding\\LangsConf\\Ini"]    ="Ini"
    libDict["\\Coding\\LangsConf\\Json"]   ="Json"



    libDict["\\SoftTuto"]              ="软件教程"

    libDict["\\SoftTuto\\Project"]                 ="工程/项目软件"
    libDict["\\SoftTuto\\Project\\AltiumDesigner"] ="Altium Designer"
    libDict["\\SoftTuto\\Project\\CadenceSPB"]     ="Cadence SPB"
    libDict["\\SoftTuto\\Project\\ModelSim"]       ="ModelSim"
    libDict["\\SoftTuto\\Project\\KeilMDK"]        ="Keil MDK"
    libDict["\\SoftTuto\\Project\\MultiSim"]       ="MultiSim"
    libDict["\\SoftTuto\\Project\\Qt"]             ="Qt"
    libDict["\\SoftTuto\\Project\\SolidWorks"]     ="SolidWorks"
    libDict["\\SoftTuto\\Project\\VisualStudio"]   ="Visual Studio"
    libDict["\\SoftTuto\\Project\\Vivado"]         ="Vivado"
    libDict["\\SoftTuto\\Project\\VSCode"]         ="VS Code"
    libDict["\\SoftTuto\\Project\\Others"]         ="其他"

    libDict["\\SoftTuto\\Image"]               ="图像图表软件"
    libDict["\\SoftTuto\\Image\\GIMP"]         ="GIMP"
    libDict["\\SoftTuto\\Image\\Mermaid"]      ="Mermaid"
    libDict["\\SoftTuto\\Image\\Origin"]       ="Origin"
    libDict["\\SoftTuto\\Image\\Solidworks"]   ="Solidworks"
    libDict["\\SoftTuto\\Image\\Visio"]        ="Visio"

    libDict["\\SoftTuto\\Animation"]                   ="动画制作软件"
    libDict["\\SoftTuto\\Animation\\SolidWorks"]       ="SolidWorks"
    libDict["\\SoftTuto\\Animation\\HTML5"]            ="HTML5"
    libDict["\\SoftTuto\\Animation\\PocketAnimation"]  ="口袋动画-Pocket Animation"

    libDict["\\SoftTuto\\Office"]          ="办公软件"
    libDict["\\SoftTuto\\Office\\Word"]    ="Word"
    libDict["\\SoftTuto\\Office\\PPT"]     ="PPT"
    libDict["\\SoftTuto\\Office\\Excel"]   ="Excel"

    libDict["\\SoftTuto\\Manage"]          ="管理类软件"
    libDict["\\SoftTuto\\Manage\\Inlook"]  ="Inlook"
    libDict["\\SoftTuto\\Manage\\Outlook"] ="Outlook"
    libDict["\\SoftTuto\\Manage\\Git"]     ="Git"

    libDict["\\SoftTuto\\Plugins"]             ="插件类"
    libDict["\\SoftTuto\\Plugins\\GIMPPlu"]    ="GIMP插件"
    libDict["\\SoftTuto\\Plugins\\OfficePlu"]  ="Office插件"
    libDict["\\SoftTuto\\Plugins\\GitbookPlu"] ="Gitbook插件"
    libDict["\\SoftTuto\\Plugins\\ChromeExt"]  ="Chrome插件"
    libDict["\\SoftTuto\\Plugins\\VSCodeExt"]  ="VSCode插件"

    libDict["\\SoftTuto\\Video"]               ="视频软件"
    libDict["\\SoftTuto\\Video\\VideoStudio"]  ="会声会影"
    
    
    # 在^^^^下面^^^^添加各级文件夹^^^
    libDict["\\KnowWorld"]                ="知识世界"
    libDict["\\KnowWorld\\SigASys"]       ="信号与系统"
    libDict["\\KnowWorld\\SigASys\\SigProc"]  ="信号处理"
    libDict["\\KnowWorld\\SigASys\\ImgProc"]  ="图像处理"
    
    summaryFileDir = "\\mds"

    print("\n正在为生成侧边栏导航,输出文件为SUMMARY.md...")
    createNavPage(summaryFileDir,libDict,libList)
    print("\n已输出文件SUMMARY.md!\n")
    

if __name__ == "__main__":
    main()