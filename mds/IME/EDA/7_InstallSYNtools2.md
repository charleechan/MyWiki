# Synopsys工具安装II-数字后端
本环境包括 `ICC`,`PT`,`Formality`。

## 安装ICC

```bash
cd [安装包目录]
mkdir /opt/eda/synopsys/icc
mkdir /opt/eda/synopsys/icc_pack
chmod 777 /opt/eda/synopsys/icc
cp ./ic_compiler_vO-2018.06-SP1/* /opt/eda/synopsys/icc_pack/

cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/icc_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/icc`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/icc`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 安装PT

```bash
cd [安装包目录]
mkdir /opt/eda/synopsys/pt
mkdir /opt/eda/synopsys/pt_pack
chmod 777 /opt/eda/synopsys/pt
cp ./pt_vO-2018.06-SP1/* /opt/eda/synopsys/pt_pack/

cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/pt_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/pt`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/pt`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 安装Formality

```bash
cd [安装包目录]
mkdir /opt/eda/synopsys/fm
mkdir /opt/eda/synopsys/fm_pack
chmod 777 /opt/eda/synopsys/fm
cp ./fm_vO-2018.06-SP1/* /opt/eda/synopsys/fm_pack/

cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/fm_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/fm`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/fm`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 修改.cshrc脚本

```bash
# 使用普通用户身份
su [你的用户名]
vim ~/.cshrc

# 在`.cshrc`文件的末尾添加如下命令：

#add ICC to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/icc/amd64/syn/bin

#add PT to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/pt/amd64/syn/bin

#add FM to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/fm/suse64/fm/bin
```

