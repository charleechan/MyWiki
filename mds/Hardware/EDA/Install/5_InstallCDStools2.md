# Cadence工具安装II-数字部分

本教程将安装INSIVE151(NC-verilog),Innovus.

本教程以root用户安装。

## 安装INCISIVE 15.10
```bash


mkdir -p /opt/eda/cadence/INCISIVE151
cd [安装包路径]
cp ./INCISIVE151/INCISIVE15.10.010_Hotfix.7z.00*  /opt/eda/cadence/
cd /opt/eda/cadence/
# 合并安装包
cat INCISIVE15.10.010_Hotfix.7z.00*>INCISIVE15.10.010_Hotfix.7z
rm -f INCISIVE15.10.010_Hotfix.7z.00*
7za x INCISIVE15.10.010_Hotfix.7z -o./
rm -f INCISIVE15.10.010_Hotfix.7z
# 运行iscape脚本,进入iscape安装界面
cd ./iscape/iscape
cd bin
./iscape.sh
```

点击 `Load directory/Media install`,选择安装包路径`/opt/eda/cadence/INCISIVE15.10.010_Hotfix`

弹出界面,勾选`incisive`, 点右下角`Next`.

弹出页面,选择所有组件,设置安装目录`/opt/eda/cadence/INCISIVE151`.

点`start`开始安装，在安装过程中弹出的对话框都写`yes`回车,碰到license不通过的写`no`回车。



## 安装INNOVUS

```bash
mkdir INNOVUS181
cd [安装包路径]
cp INNOVUS18.10.000/* /opt/eda/cadence/
cd /opt/eda/cadence/
# 解压安装包
tar xvf /opt/eda/cadence/Base_INNOVUS18.10.000_lnx86_1of2.tar
tar xvf /opt/eda/cadence/Base_INNOVUS18.10.000_lnx86_2of2.tar
rm -f Base_INNOVUS18.10.000_lnx86_*of2.tar
# 运行iscape脚本,进入iscape安装界面
cd ./iscape/iscape
cd bin
./iscape.sh
```
点击 `Load directory/Media install`,选择安装包路径`/opt/eda/cadence/INNOVUS18.10.000_lnx86.Base/CDROM1`

弹出界面,勾选`INNOVUS`, 点右下角`Next`.

弹出页面,选择所有组件,设置安装目录`/opt/eda/cadence/INNOVUS181`.

提示要不要使用默认的OpenAcess路径，建议选择默认的(输入n)就行。 


## 破解

安装完成后,开始破解.

```bash
cd /opt/eda/cadence/patch
./1patch.sh /opt/eda/cadence/INCISIVE151/
./1patch.sh /opt/eda/cadence/INNOVUS181/


# 打开用户脚本,设置环境变量
su [username]
cd ~
vim ./cshrc
# 在合适位置处,添加以下几行
setenv INCISIVE_HOME ${CADHOME}/INCISIVE151
setenv LD_LIBRARY_PATH ${INCISIVE_HOME}/tools/lib/64bit:${INCISIVE_HOME}/tools
setenv PATH ${PATH}:${INCISIVE_HOME}/tools/bin

setenv INNOVUS_HOME ${CADHOME}/INNOVUS181
setenv LD_LIBRARY_PATH ${INNOVUS_HOME}/tools/lib/64bit:${INNOVUS_HOME}/tools
setenv PATH ${PATH}:${INNOVUS_HOME}/tools/bin
```



由于上节中生成的license.dat已经包括了INCISIVE和INNOVUS,因此直接尝试运行.



在终端输入

```bash
simvision
```
可以打开 `simvision` 界面.

在终端输入

```bash
innovus
```

提示报错缺少 `libXp.so.6`,去[这里](https://pkgs.org/)搜索`libXp.so.6`,可以发现其位于`libXp`库,于是

```bash
# 安装32位libXp
yum install libXp.i686
# 安装64位libXp
yum install libXp
```

输入

```bash
innovus
```

可以打开 `innovus` 界面.
