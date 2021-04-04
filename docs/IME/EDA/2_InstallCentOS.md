
# win10安装centos7双系统

1. 准备工作：
    1.1 磁盘分区
        * 右击此电脑>>管理>>磁盘管理>>找到要压缩的盘,这里F盘**剩余空间**较大,选择F盘>>右键压缩卷>>输入要压缩的空间大小,这里输入`102400`(MB)，也就是为CentOS创建100G的空间.
        * 耐心等待,直到压缩完成.别手贱再把分出来的空间在Windows里面“添加卷”，linux安装时，只认空白硬盘。
        * 如果压缩卷过慢,你又着急的话，找一个文件少的盘符，把数据转移出去，然后直接格式化吧~
        * 使用`DiskGenius`软件，将要安装Linux的目标硬盘的分区表类型修改为GPT，具体方法可以百度。
        
    1.2 制作启动盘
        * 国内下载源和版本选择：https://blog.csdn.net/xiaojin21cen/article/details/83713559 ，这里我是为了安装IC的EDA工具,因此下载了`CentOS-6.10-x86_64-bin-DVD1_2.iso`。
        * 打开UltraISO(也叫软碟通)>>文件菜单>>打开>>选择刚下载好的ISO文件,会加载出几个文件夹>>选中在层次图的根部,也就是显示光盘图标的那个项上>>启动菜单>>写入硬盘映像>>硬盘驱动器选择U盘，写入方式改为USB-HDD+，隐藏自动分区改为无，格式化之后点击开始写入.
        * 耐心等待,直到刻录成功.
2. 开始安装
    * 笔记本bios设置U盘自启动
   
        神舟笔记本开机后，按F2进入BIOS，设置第一个启动项为U盘，选择 带有U盘标志的启动选项,例如:
        * UEFI: KingstonDataTraveler等;
        * UEFI: SanDisk等;
        * KingstonDataTraveler等;
        * USB:Generic Flash Disk等
        * USB-HDD等.
        
        > 在BIOS中设置SATA Controller Mode为AHCI模式; 设置启动选项为`UEFI Only`/`Legacy`. 关闭安全选项,等.
		
    * 安装过程
	  
        电脑重启后，进入CentOS 7菜单选项，选中Install CentOS Linux 7，按`e`键进入编辑模式后，在屏幕的最下面会出现当前运行的脚本命令。
		
        ```
        setparams 'Install CentOS Linux 7'
        
        linuxefi/images/pxeboot/vmlinuz inst.stage2=hd:LABEL=CentOS\x207\x20x86_64 quiet
        
        initrdefi/images/pxeboot/initrd.img
        ```
        
        修改其中选中的部分为
        ```
        setparams 'Install CentOS Linux 7'
        
        linuxefi/images/pxeboot/vmlinuz linux dd quiet
        
        initrdefi/images/pxeboot/initrd.img
        ```
        
        然后按`Ctrl`+`X`执行该脚本，等待执行结果，可以看到U盘所在的盘符为`sdc4`(你的可能不一样)，记下该`sdc4`，按`Ctrl`+`Alt`+`Delete`重启电脑.
        
        电脑重启后，进入CentOS 7菜单选项，选中Install CentOS Linux 7，按e键进入编辑模式，将脚本改为
        
        ```
        setparams 'Install CentOS Linux 7
        
        linuxefi/images/pxeboot/vmlinuz inst.stage2=hd:/dev/sdc4 quiet
        
        initrdefi/images/pxeboot/initrd.img
        ```
        
        这儿是指定安装U盘所在路径。然后按`Ctrl`+`X`执行该脚本。
	 
        之后出现语言选择界面，选择“中文-简体中文”

    * 安装位置
        选中`我想手动分区`,在弹出的界面点击`自动配置分区`，这时系统会默认为把最大的分区分给/home。	
        除了`swap`分区和`/boot/efi`外，其他文件系统格式都更改为ext4，Ext4 分别支持 1EB（1,048,576TB， 1EB=1024PB， 1PB=1024TB）的文件系统，以及 16TB 的文件，你的文件再大也足够用了。
        
        ```
        /　　	50G   	系统根目录
        /home	40G　　	存放所有用户文件的根目录，是用户主目录的基点，比如用户user的主目录就是/home/user.主要是桌面系统使用，     60G足够了
        /opt	200G	用户级的程序目录，额外安装的可选应用程序包所放置的位置,EDA will be installed here。
        /usr	80G	系统级的程序目录，各个用户公用的程序.
          |--lib		常用的动态链接库目录
          |--include 	包含目录,头文件目录. 
          |--doc 		Linux文档目录
          |--sbin 		超级用户的一些管理程序目录
          |--bin 		可执行二进制程序目录
          |--man 		帮助文档目录
          |--src 		源码目录,Linux源码存在于/usr/src/linux中
          |--local
        	   |--bin: 	本机系统管理员安装的 可执行二进制程序
        	   |--lib: 	本机系统管理员增加的库目录
        /swap	8G		这里需要注意的是swap的大小，一般来说，应该是实际内存的两倍，但是实际内存很大的话，设置8G也够了
        /boot	1G		存放用于系统引导时使用的各种文件.
        
        /etc			系统管理和配置文件的目录
        /bin			系统可执行二进制程序目录
        ```
        确认之后,开始自动安装.此时,可以:
        * 设置root密码,这里设置为`123`,提示过短,直接无视,连续点击左上角`完成`按钮即可.
        * 设置用户名和密码,这里用户名为姓名首字母拼音`abc`,密码同样设置`123`,并**将此账户设置为管理员**.
    * 挂载Windows硬盘到CentOS
        * 添加repo源到配置文件:`wget -O /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo`
        * 安装ntfs-3g: `yum -y install ntfs-3g`
          > 如果这里出错`file contains no head section`,你需要删除`rm -f /etc/yum.repos.d/epel.repo`,更换网络,重新添加repo源到配置文件.
        * 检查第1块硬盘并确认你要访问(挂载)的Windows硬盘上的分区：`fdisk -l /dev/sda`,检查第2块硬盘`fdisk -l /dev/sdb`，经过核对硬盘大小,这里确认挂载`sdb2`;
        * 新建目标文件夹:`mkdir /mnt/WinDiskG`
        * 将已选择的分区映射(挂载)到目标文件夹:`mount -t ntfs-3g /dev/sdb2 /mnt/WinDiskG`
        * 检查`/mnt/WinDisk`目录,查看是否已能正常访问目标分区.
        * 为了以后自动挂载分区到文件夹,需要修改配置文件:`vi /etc/fstab`.
        * 将语句`/dev/sdb2 /mnt/WinDiskG ntfs-3g defaults 0 0`添加到文件最后一行.
        * 重启即可.
		
   * 修改默认boot菜单
      * `su`以切换到root,`cd /boot/efi/EFI/centos`打开文件夹,`vim grub.cfg`打开`grub`配置选项
        * 输入`:`进入vim的命令行模式,输入`set nu`显示行号;
        * 在大概 60 多行的地方，将两个`set timeout=15`,等待时间默认 15s.
        * 110 行左右，可以看到 `menuentry` 开头,要修改启动项名称直接对单引号内内容进行修改,这里直接将`windows boot mannager`改成`Windows 10 x64 EnterPrise`.
      * `cd /boot/grub2`,打开文件夹,`vim grubenv`,将`saved_entry=Windows 10 x64 EnterPrise`,修改默认启动项为Win10系统.

      > 注意: 如果后来在保持双系统情况下,又重新安装了Windows系统,则需要在`Cent OS`中用root账户执行`grub2-mkconfig -o /boot/efi/EFI/centos/grub.cfg`重新生成boot菜单,然后才可以修改.
