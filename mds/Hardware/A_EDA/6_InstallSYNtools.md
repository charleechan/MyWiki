# Synopsys工具安装II-数字前端

本环境包括 `Synplify18`,`HiSpice`,`VCS`.

可参考[Synopsys EDA安装教程](./res/SynopsysEDA安装教程.pdf).

## 安装前的准备
新建安装目录, 建议把这种大型软件装在 `/opt/` 目录下。 

```bash
su root

# synopsys 软件安装程序 的存放目录
mkdir -p /opt/eda/synopsys/installer
# synopsys 软件安装程序 的安装包文件目录
mkdir -p /opt/eda/synopsys/installer_pack
# synplify2018 的安装目录
mkdir -p /opt/eda/synopsys/syn
# synplify2018 的安装包文件目录
mkdir -p /opt/eda/synopsys/syn_pack
# 许可程序scl 的安装目录
mkdir -p /opt/eda/synopsys/scl
# 许可程序scl 的安装包文件目录
mkdir -p /opt/eda/synopsys/scl_pack
# 存放 license.dat 文件
mkdir -p /opt/eda/synopsys/license
# 临时存放目录
mkdir -p /opt/eda/synopsys/temp

chmod 777 /opt/eda/synopsys/
chmod 777 /opt/eda/synopsys/temp
chmod 777 /opt/eda/synopsys/syn
chmod 777 /opt/eda/synopsys/scl

```
> `-p`选项是直接建立父目录。 

## 安装DC, SCL

```bash
cd [安装包目录]
# 复制 synopsysinstaller_v5.0.rar 到 /opt/eda/synopsys/installer_pack/
cp ./synopsysinstaller_v5.0.rar /opt/eda/synopsys/installer_pack/
# 复制 ./syn_vO-2018.06-SP1/* 到 /opt/eda/synopsys/syn_pack/
cp ./syn_vO-2018.06-SP1/* /opt/eda/synopsys/syn_pack/
# 复制 ./scl_v2018.06-SP1/* 到 /opt/eda/synopsys/scl_pack/
cp ./scl_v2018.06-SP1/* /opt/eda/synopsys/scl_pack/

cd /opt/eda/synopsys/installer_pack/
# 解压
unrar e synopsysinstaller_v5.0.rar
chmod +x SynopsysInstaller_v5.0.run
# 执行setup.sh
./SynopsysInstaller_v5.0.run
# 提示制定安装目录,输入
/opt/eda/synopsys/installer

# 删除 installer_pack
cd ..
rm -rf ./installer_pack
cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/syn_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/syn`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/syn`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

然后继续执行安装脚本安装scl

```bash
# 执行setup.sh
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/scl_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/scl`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/scl`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 安装HSPICE

```bash
cd [安装包目录]
mkdir /opt/eda/synopsys/hspice
mkdir /opt/eda/synopsys/hspice_pack
chmod 777 /opt/eda/synopsys/hspice
cp ./hspice_vN-2017.12-SP2/* /opt/eda/synopsys/hspice_pack/

cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/hspice_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/hspice`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/hspice`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 安装VCS

```bash
cd [安装包目录]
mkdir /opt/eda/synopsys/vcs
mkdir /opt/eda/synopsys/vcs_pack
chmod 777 /opt/eda/synopsys/vcs
cp ./vcs_vO-2018.09-SP2/* /opt/eda/synopsys/vcs_pack/

cd installer/

# 以普通用户身份安装
chmod +x setup.sh 
su [你的用户名]
./setup.sh
```

在弹出的页面中`Site ID`填写`000`, `Site Administrator`留空, C`ontact Information`填写`ccl@(none)`,点`Next`

弹出页面`Source`选`/opt/eda/synopsys/vcs_pack/`

弹出页面`Temp Path`选`/opt/eda/synopsys/temp`

弹出页面`Target Dir`选`/opt/eda/synopsys/vcs`

弹出页面勾选所有组件

弹出页面`Target Dir`选`/opt/eda/synopsys/vcs`

安装完成之后点`X`关闭页面,不要点`finish`避免出错.

## 破解
1. 找到你的`lmhostid`和 `hostname`
    >在你的 `linux` 中输入 `ifconfig` ，得到`MAC`地址,是一串12位的字符串（由0-9和a-f组成），如果得到的是几个字符串，那就随便选一个，例如是`80fa5b39ac12`。
    >在你的 `linux` 中输入 `hostname` ，得到你 `linux` 的名字，记录下来，例如是 `eda` ；

2. 在任意Windows机器上, 打开 `[安装包目录]/synopsys crark/scl_keygen.exe` 程序；把MAC地址`80fa5b39ac12`填入`HOST ID Daemon`和 `HOST ID Feature` 中，把 hostname 也就是 `eda` 填入到`HOST name`中，检查`EXPIRE`中的日期是否满足要求。
4. 点击 `Generate` 后，会在目录下生成 `Synopsys.dat` 文件，该文件就是得到的 `license` ，将该文件重命名为`license.dat`。
5. 修改`license.dat`的前3行为：

```
SERVER eda 80fa5b39ac12 27000
DAEMON snpslmd /opt/eda/synopsys/scl/suse64/bin/snpslmd
USE_SERVER
INCREMENT SSS snpslmd 1.0 12-dec-2029 1 6F52542CDB8822322E1D \
        VENDOR_STRING="28A69 CAA0B A99A7 BE9FB AD385 BDC1E 5F0F6 217B5 \
        EEC64 786" ISSUER="Synopsys, Inc. [1/8/2014 0:43:49 26356 3.16.2]" \
        NOTICE="Licensed to student@eetop [DO NOT DELETE/MODIFY SSS OR ANY \
        OTHER KEYS IN THIS FILE]" SN=RK:0:0:1
PACKAGE snps_lic_1 snpslmd 2019.2019 10A030F1A319D126BD85 COMPONENTS="3D \
        3P " ck=205
...
```

6. 将生成好的license文件导入linux系统的`/opt/eda/synopsys/license`中，执行`/opt/eda/synopsys/scl/suse64/bin/sssverify /opt/eda/synopsys/license/license.dat `可以看到`License file integrity check PASSED!`则license文件创建成功.

```bash
# 使用普通用户身份
su [你的用户名]
vim ~/.cshrc

# 在`.cshrc`文件的末尾添加如下命令：

setenv SYNOPSYS_HOME /opt/eda/synopsys
setenv LM_LICENSE_FILE ${SYNOPSYS_HOME}/license/license.dat
setenv SNPSLMD_LICENSE_FILE ${SYNOPSYS_HOME}/license/license.dat
${SYNOPSYS_HOME}/scl/suse64/bin/lmgrd -c ${SYNOPSYS_HOME}/license/license.dat -l ~/synopsys_lic.log

#add DC to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/syn/amd64/syn/bin

#add SCL to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/scl/suse64/bin

#add hspice to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/hspice/hspice/bin

#add vcs to PATH
setenv PATH ${PATH}:${SYNOPSYS_HOME}/vcs/amd64/bin
```

然后在终端执行`source ~/.cshrc`，更新环境变量.

**重启系统**

## 测试

在终端中输入`dc_shell`打开DC。

报错找不到`libtiff.so.3`,去[这里](https://rpmfind.net/)搜索`libtiff`,系统选择`centos`,下载安装64位版`	libtiff-4.0.3-35.el7.x86_64.rpm`

然后`rpm -ivh 	libtiff-4.0.3-35.el7.x86_64.rpm`,安装RPM包. 执行`sudo ln -s /usr/lib64/libtiff.so.4 /usr/lib64/libtiff.so.3`建立符号链接.

输入`dc_shell`打开DC。
