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
        sumFile.write("# Summary\n\n## [知识体系](README.md)\n")
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
    libList.append('\\Hardware')
    libList.append('\\Software')
    libList.append('\\Tricks')
    # 在^^^^上面^^^^添加一级文件夹^^^^^^^
    
    
    # 在vvvv下面vvvv添加各级文件夹vvvvvvv
    # libDict[文件夹的路径]                ="侧边栏导航名字"
    libDict["\\Hardware"]                 ="微电子专业"
    libDict["\\Hardware\\1_Devices"]        ="电磁与电子器件"
    libDict["\\Hardware\\2_SigCirSys"]      ="电路中的信号"
    libDict["\\Hardware\\3_AnalogCirciut"]  ="模拟电路基础"
    libDict["\\Hardware\\4_DigitalCircuit"] ="数字电路基础"
    libDict["\\Hardware\\5_PCB"]            ="PCB设计与应用"
    libDict["\\Hardware\\6_AnalogIC"]       ="模拟IC设计"
    libDict["\\Hardware\\7_DigitalIC"]      ="数字IC RTL设计"
    libDict["\\Hardware\\8_CPU"]            ="CPU设计"
    libDict["\\Hardware\\9_SoC"]            ="SoC设计"
    libDict["\\Hardware\\A_EDA"]            ="EDA安装"
    libDict["\\Hardware\\B_HDL"]            ="Verilog/SV"

    libDict["\\Software"]                    ="软件教程"
    libDict["\\Software\\1_CSTM32"]            ="C程序与驱动开发"
    libDict["\\Software\\2_CppQt"]             ="CPP程序与Qt开发"
    libDict["\\Software\\3_Datas"]             ="数据结构与数据库"
    libDict["\\Software\\4_DSPISP"]            ="信号/图像处理"
    libDict["\\Software\\5_PythonAI"]          ="Python与AI"
    libDict["\\Software\\6_MD"]                ="Markdown"
    libDict["\\Software\\7_HCJ"]               ="HTML/CSS/Javascript"
    libDict["\\Software\\8_H5App"]             ="HTML5移动/桌面APP"
    libDict["\\Software\\9_QML"]               ="QML(不建议学习)"


    libDict["\\Tricks"]              ="日积月累"

    libDict["\\Tricks\\Project"]                 ="工程/项目软件"
    libDict["\\Tricks\\Project\\AltiumDesigner"] ="Altium Designer"
    libDict["\\Tricks\\Project\\CadenceSPB"]     ="Cadence SPB"
    libDict["\\Tricks\\Project\\ModelSim"]       ="ModelSim"
    libDict["\\Tricks\\Project\\KeilMDK"]        ="Keil MDK"
    libDict["\\Tricks\\Project\\MultiSim"]       ="MultiSim"
    libDict["\\Tricks\\Project\\Qt"]             ="Qt"
    libDict["\\Tricks\\Project\\SolidWorks"]     ="SolidWorks"
    libDict["\\Tricks\\Project\\VisualStudio"]   ="Visual Studio"
    libDict["\\Tricks\\Project\\Vivado"]         ="Vivado"
    libDict["\\Tricks\\Project\\VSCode"]         ="VS Code"
    libDict["\\Tricks\\Project\\Others"]         ="其他"

    libDict["\\Tricks\\Image"]               ="图像图表软件"
    libDict["\\Tricks\\Image\\GIMP"]         ="GIMP"
    libDict["\\Tricks\\Image\\Origin"]       ="Origin"
    libDict["\\Tricks\\Image\\Visio"]        ="Visio"

    libDict["\\Tricks\\Office"]          ="办公软件"
    libDict["\\Tricks\\Office\\Word"]    ="Word"
    libDict["\\Tricks\\Office\\PPT"]     ="PPT"
    libDict["\\Tricks\\Office\\Excel"]   ="Excel"

    libDict["\\Tricks\\Manage"]          ="管理类软件"
    libDict["\\Tricks\\Manage\\Inlook"]  ="Inlook"
    libDict["\\Tricks\\Manage\\Git"]     ="Git"

    libDict["\\Tricks\\Plugins"]             ="插件类"
    libDict["\\Tricks\\Plugins\\GIMPPlu"]    ="GIMP插件"
    libDict["\\Tricks\\Plugins\\OfficePlu"]  ="Office插件"
    libDict["\\Tricks\\Plugins\\GitbookPlu"] ="Gitbook插件"
    libDict["\\Tricks\\Plugins\\ChromeExt"]  ="Chrome插件"
    libDict["\\Tricks\\Plugins\\VSCodeExt"]  ="VSCode插件"

    libDict["\\Tricks\\Video"]               ="视频软件"
    libDict["\\Tricks\\Video\\VideoStudio"]  ="会声会影"
    
    libDict["\\Tricks\\Music"]               ="音频软件"

    libDict["\\Tricks\\Game"]                ="游戏"
    # 在^^^^下面^^^^添加各级文件夹^^^

    
    summaryFileDir = "\\mds"

    print("\n正在为生成侧边栏导航,输出文件为SUMMARY.md...")
    createNavPage(summaryFileDir,libDict,libList)
    print("\n已输出文件SUMMARY.md!\n")
    

if __name__ == "__main__":
    main()