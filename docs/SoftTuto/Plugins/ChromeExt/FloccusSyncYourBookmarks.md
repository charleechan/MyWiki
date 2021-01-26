## Floccus配合坚果云同步书签教程
Floccus支持WebDAV、Nextcloud Bookmarks和本地文件网盘同步。这里配合坚果云,采用的是WebDAV方案.

## 在坚果云上的准备
在同步文件夹根目录(也就是`我的坚果云`同一目录)下创建一个文件夹，选择默认不同步到本地，你要同步也可以，名字随意，这里是 floccus.

然后上传一个[bookmarks.xbel](./res/bookmarks.xbel)文件到刚新建的文件夹里面.

接着坚果云`账户信息`-`安全选项`-`第三方应用管理`，创建一个WebDAV应用，获取密码。

## Floccus插件安装和设置

安装好了Floccus插件后，点击图标，然后选择XBEL in WebDAV，然后Add Account。

WebDAV的服务器信息就跟着坚果云给你的信息填写上去就可以了,一般应该是:

```python
## WebDAV URL:
https://dav.jianguoyun.com/dav/
## User name:
*****@***.com
## Password:
*****
## Bookmarks file path,填写你刚才创建的
文件夹/bookmarks.xbel
```

书签的目录直接选择`根目录`就可以了，如果新建的话他是在你现在浏览器书签基础上新建一个同步的书签文件夹。

例如,在PC端Edge里选择根目录为`/收藏夹栏/`,在Android端的**kiwi browser**里选择`/移动设备书签/`就可以啦.

