# 在Markdown中使用FontAwesome

## 准备
要在 Markdown 文档中输入 `Font Awesome`，需要在文档中任意位置贴粘入如下语句（可以放在文档结尾处，以不影响直接在 Markdown 文档中的阅读）.

```
<head> 
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/all.js"></script> 
    <script defer src="https://use.fontawesome.com/releases/v5.0.13/js/v4-shims.js"></script> 
</head> 
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.13/css/all.css">
```

## 获取符号名称
在[符号列表](https://fontawesome.com/icons?d=gallery&m=free)中搜索,获得符号编码.


之后就可以直接插入了,代码
`<i class="fa fa-weixin"></i>`<i class="fa fa-arrow-circle-right"></i>&nbsp;&nbsp;<i class="fa fa-weixin"></i>

## 符号格式

### 尺寸
可选项`fa-xs`,`fa-sm`,`fa-lg`,`fa-2x`,`fa-3x`,`...`,`fa-10x`

`<i class="fa fa-weixin fa-2x"></i>` <i class="fa fa-arrow-circle-right"></i>&nbsp;&nbsp;<i class="fa fa-weixin fa-2x"></i>

### 转动

`<i class="fa fa-spin fa-weixin"></i>`<i class="fa fa-arrow-circle-right"></i>&nbsp;&nbsp;<i class="fa fa-spin fa-weixin"></i>


### 首字下沉

`<i class="fa fa-quote-left fa-3x fa-pull-left">A</i>is the first letter in alphabet.`

<i class="fa fa-arrow-circle-down"></i>

<i class="fa fa-quote-left fa-3x fa-pull-left">A</i>is the first letter in alphabet.






---
### 文末彩蛋
两张并排的图片
```
<figure class="half">
    <img src="path/to/img1.png" width="20px">
    <img src="path/to/img2.png" width="20px">
</figure>
```
对应的显示
<figure class="half">
    <img src="https://charleechan.github.io/MyWiki/img/logo.png" width="20px">
    <img src="https://charleechan.github.io/MyWiki/img/logo.png" width="20px">
</figure>


