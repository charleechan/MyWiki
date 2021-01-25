# -*- using: utf-8 -*-

import os
import sys
# 本文件功能: 一键生成导航

# 第一种方式
def recu_list_dirs_by_dictionary_order(path, indent = 0, maxi = -1):
    '''
        按字典序递归输出目录结构
        :param path:   str 文件路径
        :param indent: int 首次缩进空格(默认为 0，一般不用改变)
        :param maxi:   int 最大展开层数(默认为 -1，表示全部展开)
    '''
    if maxi != 0:
        try:
            lsdir = os.listdir(path)
        except PermissionError: # 对于权限不够的文件不作处理
            pass
        else:
            for item in lsdir:
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    print(' ' * indent, '+', item)
                    recu_list_dirs_by_dictionary_order(full_path, indent + 4, maxi - 1)
                if os.path.isfile(full_path):
                    print(' ' * indent, '-', item)
# 第二种方式
def recu_list_dirs_by_file_type(path,dstfile,dstpath="", indent = 0, maxi = -1):
    '''
        按文件类型递归输出目录结构,写入到文件中
        :param path:   str 文件路径
        :param indent: int 首次缩进空格(默认为 0，一般不用改变)
        :param maxi:   int 最大展开层数(默认为 -1，表示全部展开)
        :param dstfile: 目标文件 已经打开
    '''

    if dstpath =="":
        dstpath = path
    if maxi != 0:
        try:
            lsdir = os.listdir(path)
        except PermissionError: # 对于权限不够的文件不作处理
            pass
        else:
            dirs = [item for item in lsdir if os.path.isdir(os.path.join(path, item))]
            files = [item for item in lsdir if os.path.isfile(os.path.join(path, item))]
            for item in files:
                if not item=="README.md":
                    file_name = os.path.splitext(item)[0]

                    if dstpath == path:
                        trimPath = ""
                    else:
                        trimPath=path.replace(dstpath+"\\","")+"/"
                        trimPath=trimPath.replace("\\","/")

                    dstStr = ' ' * indent + '* [' + file_name + "](" +trimPath+ file_name + ".html)"
                    # print(dstStr)
                    dstfile.write(dstStr+"\n")
            for item in dirs:
                dstStr = ' ' * indent + '* [' + item + "](" + item + "/index.html)"
                # print(dstStr)
                dstfile.write(dstStr+"\n")
                recu_list_dirs_by_file_type(os.path.join(path, item),dstfile,dstpath, indent + 2, maxi - 1)


def recu_list_dirs_by_file_type1(path,dstfile,dstpath="", indent = 0, maxi = -1):
    '''
        按文件类型递归输出目录结构,写入到文件中
        :param path:   str 文件路径
        :param indent: int 首次缩进空格(默认为 0，一般不用改变)
        :param maxi:   int 最大展开层数(默认为 -1，表示全部展开)
        :param dstfile: 目标文件 已经打开
    '''

    if dstpath =="":
        dstpath = path
    if maxi != 0:
        try:
            lsdir = os.listdir(path)
        except PermissionError: # 对于权限不够的文件不作处理
            pass
        else:
            dirs = [item for item in lsdir if os.path.isdir(os.path.join(path, item))]
            files = [item for item in lsdir if os.path.isfile(os.path.join(path, item))]
            for item in files:
                if not item=="README.md":
                    file_name = os.path.splitext(item)[0]

                    if dstpath == path:
                        trimPath = ""
                    else:
                        trimPath=path.replace(dstpath+"\\","")+"/"
                        trimPath=trimPath.replace("\\","/")

                    dstStr = ' ' * indent + '* [' + file_name + "](" +trimPath+ file_name + ".html)"
                    # print(dstStr)
                    dstfile.write(dstStr+"\n")
            for item in dirs:
                dstStr = ' ' * indent + '* [' + item + "](" + item + "/index.html)"
                # print(dstStr)
                dstfile.write(dstStr+"\n")
                recu_list_dirs_by_file_type1(os.path.join(path, item),dstfile,dstpath, indent + 2, maxi - 1)

def recu_list_subdirs(path,retList,dstPath=""):
    # 列出某目录下的文件
    if(dstPath==""):
        dstPath = path
    for lists in os.listdir(path):  
        # 连接文件名到路径     
        curPath = os.path.join(path, lists)
        # 如果是文件,且文件名匹配
        if os.path.isdir(curPath):
            
            trimPath=curPath.replace(dstPath+"\\","")+"/"
            trimPath=trimPath.replace("\\","/")
            retList.append(curPath)
            recu_list_subdirs(curPath,retList,dstPath)


# 更新路径rootDir下的名字为filename的文件,内容包含本文件夹下的目录树
def Update(rootDir, filename):  
    global langHead 
    # 列出某目录下的文件
    for lists in os.listdir(rootDir):  
        # 连接文件名到路径     
        path = os.path.join(rootDir, lists)
        # 如果是文件,且文件名匹配
        if os.path.isfile(path) and os.path.basename(path) == filename:
            try:
                # 找到当前文件的物理路径
                realpath = os.path.realpath(path)
                # 找到当前文件的物理目录
                currentdir = os.path.dirname(realpath)
                # 打开当前文件
                with open(path,mode="w", encoding='utf_8') as f:
                    f.write("\n# 目录列表\n")
                    recu_list_dirs_by_file_type1(currentdir,f)
                    # 建立当前目录的脑图结构
                    f.write("\n\n```"+ langHead +"\n")
                    recu_list_dirs_by_file_type(currentdir,f)
                    f.write("```\n")



            except:
                print('error: ', path, '\n')
def createNavPage(libList):
    filepath = __file__
    realpath = os.path.realpath(filepath)
    current_path = os.path.dirname(realpath)
    
    for libdir in libList:
        cur_path = current_path+libdir
        retList = []
        retList.append(cur_path)
        recu_list_subdirs(cur_path,retList)
        for item in retList:
            # print(item)
            Update(item, "README.md")


def main():
    libList = []
    libList.append('\\mds\\Coding')
    libList.append('\\mds\\SoftTuto')
    libList.append('\\mds\\OtherLibs')
    global langHead
    langHead = "mind:height=300,title=内容概要,color"

    createNavPage(libList)
    

if __name__ == "__main__":
    main()