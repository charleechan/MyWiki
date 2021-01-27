HTML(Hyper Text Markup Language, 超文本标记语言)的基础知识
```markmap
* HTML基础
  * 目的: 由浏览器解析、渲染成网页
  * 文件后缀: `.html`和`.htm`无区别
  * 基本元素: 由`<`和`>`指定`tag`标签,通常成对出现**开始标签和结束标签**,如`<b>`和`</b>`
  * 元素特点: 成对; 可嵌套; 空元素(`<tag>`和`</tag>`之间无内容)在开始标签关闭元素; **请小写.**
  * 元素属性: 用于定义元素的特点,格式`name="MyName"`,值应使用单引号或双引号包围起来.
  * 开发环境
    * 编辑器: `VS Code`,编辑完成后直接双击打开.
    * 调试: 浏览器按`F12`
  * 文档结构
    * `<!DOCTYPE html>`声明文档类型,方便浏览器解析
    * `<html>`是页面的**根元素**
    * `<head>`包含元(meta)数据,*不显示*
      * `<meta charset="utf-8">`定义编码格式
      * `<meta name="keywords" content="HTML, CSS">`为搜索引擎定义关键词
      * `<meta http-equiv="refresh" content="30">` 定义自动刷新间隔
      * `<title>`定义网页标题
      * `<base>`设置本网页默认的链接目标,写法同`<a>`
    * `<body>`网页内容,*显示*
      * `<h1>`1级大标题,支持`<h1>`,`<h2>`,`...`,`<h6>`
      * `<p>`段落
      * 样式设置
        * 内联样式
          * `<body>`中的元素通过`style`属性设置:`<p style="color:blue;">我是段落</p>`
        * 内部样式
          * 在`<head>`中添加`<style type="text/css>body{color:black}</style>`
        * 外部样式表
          *  `<head>`添加`<link rel="stylesheet" type="text/css" href="style.css">`链接外部样式
        * 常用样式(可应用到文本等大部分元素)
          * 背景
            * 背景颜色`background-color:red;`
          * 文本
            * 字体`font-family:arial;`
            * 文本颜色`color:red;`
            * 文本尺寸`font-size:20px;`
            * 对齐`text-align:center;`
      * 常用属性(大部分元素)
        * `class`
          * 定义元素的类型名(用于从样式文件中设置样式)
        * `id`
          * 定义元素的ID(用于设置样式,JS读取并设置等)
        * `style`
          * 定义元素的行内样式
        * `title`
          * 定义元素的额外信息(工具条)
      * 链接
        * `<a href="https://www.xxx.xxx#idvalue target="_blank">链接文本</a>`
        * 链接发起者可以是`文本`,`图像`,或其他HTML元素.
        * `herf`属性
          * `#idvalue`链接到目标页面中`id=idvalue`的元素的位置.
          * `herf="#idvalue`将链接到当前页的相应元素位置.
          * 发邮件`herf=mailto:aa@xx.com?Subject=Hello%20again`
        * `target`定义显示到:`_blank`新窗口,`_top`跳出框架
      * 图像(空元素)
        * `<img loading="logo" src="/img/logo.png" width="100" height="100"/>`
        * 属性`border`定义边框宽度,如`border="0"`
        * 属性`alt`定义替代文本,如`alt="logo.png"`
        * 使用`style="align:top"`定义图片顶部与文本对齐
        * 使用`style="float:right"`定义浮动在文本的右边
        * 使用`<map>`和`<area>`为图像分块设置链接.
        * 当网页图片过多,加载会很慢,慎用图片!
      * 文本
        * 换行,水平线,注释
          * `<br/>`,`<hr/>``<!-- 我是注释 -->`
        * 加粗,斜体,上下标
          * `<b>加粗</b>`,`<i>斜体</i>`,`<sub>下标</sub>`,`<sup>上标</sup>`
        * 着重,加重,下划线,删除线
          * `<em>着重</em>`,`<strong>加重</strong>`,`<ins>下划线</ins>`,`<del>删除线</del>`
        * 代码,键盘
          * `<code>代码</code>`,`<kbd>键盘</kbd>`
      * 表格
        * `<table border="1" cellspacing="0" cellpadding="10">`定义表格,设置边界,单元格间距,单元格边距
        * `<caption>Table 1.aa</caption>`定义表格的标题
        * `<tr></tr>`定义一个行
        * `<th>Header</th>`定义表头(一般会在第一行/列定义,会自动加粗居中)
        * `<td>I'm in a cell</td>`定义一个单元格
        * `colspan="2"`和`rowspan="2"`可以设置一个跨2行/列的单元格
      * 列表
        * `<ul><li>item1</li><li>item2</li></ul>`定义无序列表
          * `style="list-style-type:disc"`定义列表样式
        * `<ol><li>item1</li><li>item2</li></ul>`定义有序列表
          * `type="A"`定义列表样式为大写字母列表
      * `<div>`容器
        * 用于对大的内容块设置样式属性
        * 用于文档布局
          * `style="background-color:#EEEEEE;height:200px;width:400px;float:left;"`
      * 表单
        * `<form></form>`创建表单
        * `<fieldset><legend>Title</legend></fieldset>`设置表单的外框及Title
        * `<input>`用于输入的元素
          * `<input type="text" name="firstname">`文本输入框
          * `<input type="password" name="pwd">`密码输入框
          * `<input type="radio" name="sex" value="female">`单选输入
          * `<input type="checkbox" name="vehicle" value="Bike">`复选输入
          * `<input type="submit" value="Submit">`提交按钮
        * `<select name="cars"><option value="saab">Saab</option></select>`多选框
        * `<button></button>`设置按钮
      * 框架(嵌套显示多个页面)
        * `<iframe src="URL" name="iframe_a"></iframe>`第一个框架显示URL页面
        * `<a href="http://www.runoob.com" target="iframe_a">RUNOOB.COM</a>`该超链接将更新框架内的内容
      * 颜色
        * `R,G,B`表示颜色值,`rgb(255,0,17)`
        * 十六进制,六位表示,`#FF0011`
        * 十六进制,三位`#RGB`,等价于`#RRGGBB`
      * `<script></script>`脚本
        * `document.write("<p>嘿嘿</p>")`输出到HTML流
        * `btnFun()`定义按钮事件响应
        * `document.getElementById("demo").style.color="#ff0000";`修改文档样式
      * 转义字符
        * `&nbsp;` ` `(Non-breaking Space)
        * `&lt;` `<`(less than, 小于)
        * `&gt;` `>`(great than, 大于)
        * `&amp;` `&` (ampersand, 表示and的符号)
        * `&quot;` `"`(quote, 引号)
        * `&sect;` `§` (section, 小节)
        * `&copy;` `©` (copyright,版权)
        * `&reg;` `®` (register,注册商标)
        * `&times;` `×` (times, 乘号)
        * `&divide;` `÷` (divide, 除号)
```


## 饭后甜点
* [HTML速查](https://www.runoob.com/html/html-quicklist.html)