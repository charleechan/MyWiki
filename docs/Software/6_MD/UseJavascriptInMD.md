# 在Markdown中使用Javascript
在VS code的Markdown Preview Enhanced中,不会实时渲染,但是在`Gitbook`生成的`html`中已经可以实时渲染.

## 插入wavedrom时序图

在`Markdown`文件的末尾放入以下代码

```html
<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/skins/default.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/wavedrom.min.js" type="text/javascript"></script>
<body onload="WaveDrom.ProcessAll()">
```

在要插入时序图的位置,插入以下代码
```html
<script type="WaveDrom">
{signal: [
  {name: "Alfa", wave: "01.zx=ud.23.456789" },
  {name: 'clk', wave: 'p.....|P..'},
  {name: 'dat', wave: 'x.345x|=.x', data: ['head', 'body', 'tail', 'data']},
  {name: 'req', wave: '0.1..0|1.0'},
  {name: 'ack', wave: '1.....|01.'}
]}
</script>
```

渲染效果:
<script type="WaveDrom">
{signal: [
  {name: "Alfa", wave: "01.zx=ud.23.456789" },
  {name: 'clk', wave: 'p.....|P..'},
  {name: 'dat', wave: 'x.345x|=.x', data: ['head', 'body', 'tail', 'data']},
  {name: 'req', wave: '0.1..0|1.0'},
  {name: 'ack', wave: '1.....|01.'}
]}
</script>


<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/skins/default.js" type="text/javascript"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/wavedrom/2.6.8/wavedrom.min.js" type="text/javascript"></script>
<body onload="WaveDrom.ProcessAll()">