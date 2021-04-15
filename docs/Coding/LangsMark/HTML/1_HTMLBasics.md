# HTML的基础知识

(Hyper Text Markup Language, 超文本标记语言)

```mind:height=700,title=内容概要,color
* HTML基础
  * 目的: 由浏览器解析、渲染成网页
  * 文件后缀: .html和.htm无区别
  * 基本元素: 由&lt;和&gt;指定tag标签,通常成对出现**开始标签和结束标签**,如&lt;b&gt;和&lt;/b&gt;
  * 元素特点: 成对; 可嵌套; 空元素(&lt;tag&gt;和&lt;/tag&gt;之间无内容)在开始标签关闭元素; **请小写.**
  * 元素属性: 用于定义元素的特点,格式name="MyName",值应使用单引号或双引号包围起来.
  * 开发环境
    * 编辑器: VS Code,编辑完成后直接双击打开.
    * 调试: 浏览器按F12
  * 文档结构
    * &lt;!DOCTYPE html&gt;声明文档类型,方便浏览器解析
    * &lt;html&gt;是页面的**根元素**
    * &lt;head&gt;包含元(meta)数据,*不显示*
      * &lt;meta charset="utf-8"&gt;定义编码格式
      * &lt;meta name="keywords" content="HTML, CSS"&gt;为搜索引擎定义关键词
      * &lt;meta http-equiv="refresh" content="30"&gt; 定义自动刷新间隔
      * &lt;title&gt;定义网页标题
      * &lt;base&gt;设置本网页默认的链接目标,写法同&lt;a&gt;
    * &lt;body&gt;网页内容,*显示*
      * &lt;h1&gt;1级大标题,支持&lt;h1&gt;,&lt;h2&gt;,...,&lt;h6&gt;
      * &lt;p&gt;段落
      * 样式设置
        * 内联样式
          * &lt;body&gt;中的元素通过style属性设置:&lt;p style="color:blue;"&gt;我是段落&lt;/p&gt;
        * 内部样式
          * 在&lt;head&gt;中添加&lt;style type="text/css&gt;body{color:black}&lt;/style&gt;
        * 外部样式表
          *  &lt;head&gt;添加&lt;link rel="stylesheet" type="text/css" href="style.css"&gt;链接外部样式
        * 常用样式(可应用到文本等大部分元素)
          * 背景
            * 背景颜色background-color:red;
          * 文本
            * 字体font-family:arial;
            * 文本颜色color:red;
            * 文本尺寸font-size:20px;
            * 对齐text-align:center;
      * 常用属性(大部分元素)
        * class
          * 定义元素的类型名(用于从样式文件中设置样式)
        * id
          * 定义元素的ID(用于设置样式,JS读取并设置等)
        * style
          * 定义元素的行内样式
        * title
          * 定义元素的额外信息(工具条)
      * 链接
        * &lt;a href="https://www.xxx.xxx#idvalue target="_blank"&gt;链接文本&lt;/a&gt;
        * 链接发起者可以是文本,图像,或其他HTML元素.
        * herf属性
          * #idvalue链接到目标页面中id=idvalue的元素的位置.
          * herf="#idvalue将链接到当前页的相应元素位置.
          * 发邮件herf=mailto:aa@xx.com?Subject=Hello%20again
        * target定义显示到:_blank新窗口,_top跳出框架
      * 图像(空元素)
        * &lt;img loading="logo" src="/img/logo.png" width="100" height="100"/&gt;
        * 属性border定义边框宽度,如border="0"
        * 属性alt定义替代文本,如alt="logo.png"
        * 使用style="align:top"定义图片顶部与文本对齐
        * 使用style="float:right"定义浮动在文本的右边
        * 使用&lt;map&gt;和&lt;area&gt;为图像分块设置链接.
        * 当网页图片过多,加载会很慢,慎用图片!
      * 文本
        * 换行,水平线,注释
          * &lt;br/&gt;,&lt;hr/&gt;&lt;!-- 我是注释 --&gt;
        * 加粗,斜体,上下标
          * &lt;b&gt;加粗&lt;/b&gt;,&lt;i&gt;斜体&lt;/i&gt;,&lt;sub&gt;下标&lt;/sub&gt;,&lt;sup&gt;上标&lt;/sup&gt;
        * 着重,加重,下划线,删除线
          * &lt;em&gt;着重&lt;/em&gt;,&lt;strong&gt;加重&lt;/strong&gt;,&lt;ins&gt;下划线&lt;/ins&gt;,&lt;del&gt;删除线&lt;/del&gt;
        * 代码,键盘
          * &lt;code&gt;代码&lt;/code&gt;,&lt;kbd&gt;键盘&lt;/kbd&gt;
      * 表格
        * &lt;table border="1" cellspacing="0" cellpadding="10"&gt;定义表格,设置边界,单元格间距,单元格边距
        * &lt;caption&gt;Table 1.aa&lt;/caption&gt;定义表格的标题
        * &lt;tr&gt;&lt;/tr&gt;定义一个行
        * &lt;th&gt;Header&lt;/th&gt;定义表头(一般会在第一行/列定义,会自动加粗居中)
        * &lt;td&gt;I'm in a cell&lt;/td&gt;定义一个单元格
        * colspan="2"和rowspan="2"可以设置一个跨2行/列的单元格
      * 列表
        * &lt;ul&gt;&lt;li&gt;item1&lt;/li&gt;&lt;li&gt;item2&lt;/li&gt;&lt;/ul&gt;定义无序列表
          * style="list-style-type:disc"定义列表样式
        * &lt;ol&gt;&lt;li&gt;item1&lt;/li&gt;&lt;li&gt;item2&lt;/li&gt;&lt;/ul&gt;定义有序列表
          * type="A"定义列表样式为大写字母列表
      * &lt;div&gt;容器
        * 用于对大的内容块设置样式属性
        * 用于文档布局
          * style="background-color:#EEEEEE;height:200px;width:400px;float:left;"
      * 表单
        * &lt;form&gt;&lt;/form&gt;创建表单
        * &lt;fieldset&gt;&lt;legend&gt;Title&lt;/legend&gt;&lt;/fieldset&gt;设置表单的外框及Title
        * &lt;input&gt;用于输入的元素
          * &lt;input type="text" name="firstname"&gt;文本输入框
          * &lt;input type="password" name="pwd"&gt;密码输入框
          * &lt;input type="radio" name="sex" value="female"&gt;单选输入
          * &lt;input type="checkbox" name="vehicle" value="Bike"&gt;复选输入
          * &lt;input type="submit" value="Submit"&gt;提交按钮
        * &lt;select name="cars"&gt;&lt;option value="saab"&gt;Saab&lt;/option&gt;&lt;/select&gt;多选框
        * &lt;button&gt;&lt;/button&gt;设置按钮
      * 框架(嵌套显示多个页面)
        * &lt;iframe src="URL" name="iframe_a"&gt;&lt;/iframe&gt;第一个框架显示URL页面
        * &lt;a href="http://www.runoob.com" target="iframe_a"&gt;RUNOOB.COM&lt;/a&gt;该超链接将更新框架内的内容
      * 颜色
        * R,G,B表示颜色值,rgb(255,0,17)
        * 十六进制,六位表示,#FF0011
        * 十六进制,三位#RGB,等价于#RRGGBB
      * &lt;script&gt;&lt;/script&gt;脚本
        * document.write("&lt;p&gt;嘿嘿&lt;/p&gt;")输出到HTML流
        * btnFun()定义按钮事件响应
        * document.getElementById("demo").style.color="#ff0000";修改文档样式
      * 转义字符
        * &nbsp;  (Non-breaking Space)
        * &lt; &lt;(less than, 小于)
        * &gt; &gt;(great than, 大于)
        * &amp; & (ampersand, 表示and的符号)
        * &quot; "(quote, 引号)
        * &sect; § (section, 小节)
        * &copy; © (copyright,版权)
        * &reg; ® (register,注册商标)
        * &times; × (times, 乘号)
        * &divide; ÷ (divide, 除号)
```


## 饭后甜点
* [HTML速查](https://www.runoob.com/html/html-quicklist.html)