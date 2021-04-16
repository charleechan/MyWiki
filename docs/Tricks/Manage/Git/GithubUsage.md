# 使用Github的基本流程

## 下载Git
    搜索“Git”，在官网中根据系统版本下载，并双击打开，按默认已勾选组件点下一步;
    勾选在Windows命令行窗口中使用Git；
    使用推荐的OpenSSL库用于HTTPS连接；
    一路默认安装即可。
	
## 配置SSH Key

1.如果C:\uers\[user] 没有.ssh文件夹，需要创建SSH Key：
	ssh-keygen -t rsa -C "charleechan@163.com"

2.把生成的key填写到Github中,在右上角头像的Settings的SSH and GPG keys那里填,title随便写,主要是用来注明的

	使用命令 `clip < ~/.ssh/id_rsa.pub` 把刚才id_rsa.pub里面的内容复制到Title下面的Key内容框里面
	
## 使用Git 命令创建仓库

1. 新建本地仓库

    双击打开Git Bash，配置你的GitHub用户：
    ```
	git config --global user.name "charleechan"
    git config --global user.email "charleechan@163.com"
	```
    键入你要新建仓库的位置，如：`cd /d/Code/charleechan.github.io`
    开始创建代码仓库：`git init`

2. 关联远程仓库

    新建远程仓库，注意不要勾选添加Readme!!!!!注意不要勾选添加Readme!!!!!注意不要勾选添加Readme!!!!!


	首先与远程库创建关联：`git remote add origin https://github.com/[Github用户名]/[仓库名]`或`git remote add origin git@github.com:charleechan/charleechan.github.io.git`

	> 在创建好Github仓库后有两个地址,一个是https的地址,另一个是SSH地址,也就是上面这个地址. 

	切换到分支git checkout -b main,其中main是分支名

	如果勾选了，你需要先将远程库的文件合并到本地库：`git pull --rebase origin main` ,其中main是分支名
  
3. 在该文件夹下新建代码文件即可，这里方便测试，新建test.txt，输入命令
    * `git add .`		添加所有文件
    * `git add test.txt`		添加单个文件
    * `git status`		查看git状态
    * `git commit -m "It's my Test WebPage file."`  

4. 上传到仓库(首次上传需要登陆账户密码)：`git push -u origin main`	(执行这个之前必须先在本地做一次提交操作,其中main是分支名)
	
5. 查看上传日志: `git log`

## 更进一步

当然, 有很多时候,我们需要忽略本地特定目录下的文件,例如:Python的依赖库`PyhtonLibs`,或者node.js的组件`node_modules`文件夹都不需要上传到github,这时,要设置**忽略文件夹**:

1. 在`git bash`中输入`touch .gitignore`,新建一个文件`.gitignore`;
2. 可以使用notepad++或VS code编辑该文件,在其中添加
   ```
   ./node_modules/
   ```
   注意尽量在最后添加`/`
3. 分别执行以下命令
```
git rm -r --cached .
git add .
git commit -m "update .gitignore"
```

## Github Host更新及常见问题

1. Hosts文件

```bash
# Github Hosts
# Update 20210312
140.82.112.3 github.com
140.82.112.10 nodeload.github.com
140.82.114.6 api.github.com
13.229.189.0 codeload.github.com
185.199.110.133 raw.github.com
185.199.110.153 training.github.com
185.199.110.153 assets-cdn.github.com
185.199.110.153 documentcloud.github.com
185.199.110.154 help.github.com

185.199.110.153 githubstatus.com
199.232.69.194 github.global.ssl.fastly.net

185.199.110.133 raw.githubusercontent.com
185.199.110.133 cloud.githubusercontent.com
185.199.110.133 gist.githubusercontent.com
185.199.110.133 marketplace-screenshots.githubusercontent.com
185.199.110.133 repository-images.githubusercontent.com
185.199.110.133 user-images.githubusercontent.com
185.199.110.133 desktop.githubusercontent.com

185.199.110.133 avatars.githubusercontent.com
185.199.110.133 avatars0.githubusercontent.com
185.199.110.133 avatars1.githubusercontent.com
185.199.110.133 avatars2.githubusercontent.com
185.199.110.133 avatars3.githubusercontent.com
185.199.110.133 avatars4.githubusercontent.com
185.199.110.133 avatars5.githubusercontent.com
185.199.110.133 avatars6.githubusercontent.com
185.199.110.133 avatars7.githubusercontent.com
185.199.110.133 avatars8.githubusercontent.com
# End of the section
```

1. 问题: 使用`git`命令显示错误`fatal: unable to access '××': OpenSSL SSL_read: SSL_ERROR_SYSCALL, errno 10054`
解决办法:
首先执行命令`git config http.sslVerify "false"`, 若出现错误`fatal: not in a git directory`,则继续执行`git config --global http.sslVerify "false"`即可.
