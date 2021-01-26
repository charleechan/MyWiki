## 使用WaveDrom画时序图或电路图

[WaveDrom.js](https://wavedrom.com/)是一个JS脚本.

代码块标识: wavedrom
### 时序图
signal元素是波形图的数组,包含若干个波形.

* 每个波形图至少包含两个域,分别是信号名`name`和波形数据`wave`.
* wave字符串中的每个字符都代表了一个时钟周期.
* `.`: 延续上一周期的状态.

`wave`中的字符中,用于时钟信号的值:
* `p`: 上升沿开始的时钟信号(50%);
* `P`: 带箭头的、上升沿开始的时钟信号(50%);
* `n`: 下降沿沿开始的时钟信号(50%);
* `N`: 带箭头的、下降沿开始的时钟信号(50%);
* `h`: 高电平,如果有跳变,边沿是平的.
* `H`: 带箭头的、高电平.
* `l`: 低电平,如果有跳变,边沿是平的.
* `L`: 带箭头的、低电平.

`wave`中的字符中,用于数据信号的值:
* `0`: 低电平,如果有跳变,边沿是斜的.
* `1`: 高电平,如果有跳变,边沿是斜的.
* `x`: 不确定.
* `z`: 高阻态.
* `u`: exp型上升线.
* `d`: exp型下降线.
* `=`: 引用data域的字符,背景色为白色.
* `2`: 引用data域的字符,背景色透明.
* `3/4/5/6/7/8/9`: 引用data域的字符,并加不同的背景色


==[gitbook 的 wavedrom插件](https://www.npmjs.com/package/gitbook-plugin-wavedrom)目前有错, 后续我改改看看咋更新.==

代码块标识: wavedrom
### 时序图
signal元素是波形图的数组,包含若干个波形.

* 每个波形图至少包含两个域,分别是信号名`name`和波形数据`wave`.
* wave字符串中的每个字符都代表了一个时钟周期.
* `.`: 延续上一周期的状态.

`wave`中的字符中,用于时钟信号的值:
* `p`: 上升沿开始的时钟信号(50%);
* `P`: 带箭头的、上升沿开始的时钟信号(50%);
* `n`: 下降沿沿开始的时钟信号(50%);
* `N`: 带箭头的、下降沿开始的时钟信号(50%);
* `h`: 高电平,如果有跳变,边沿是平的.
* `H`: 带箭头的、高电平.
* `l`: 低电平,如果有跳变,边沿是平的.
* `L`: 带箭头的、低电平.

`wave`中的字符中,用于数据信号的值:
* `0`: 低电平,如果有跳变,边沿是斜的.
* `1`: 高电平,如果有跳变,边沿是斜的.
* `x`: 不确定.
* `z`: 高阻态.
* `u`: exp型上升线.
* `d`: exp型下降线.
* `=`: 引用data域的字符,背景色为白色.
* `2`: 引用data域的字符,背景色透明.
* `3/4/5/6/7/8/9`: 引用data域的字符,并加不同的背景色

### 综合

```json
{signal: [
  {name: "Alfa", wave: "01.zx=ud.23.456789" },
  {name: 'clk', wave: 'p.....|P..'},
  {name: 'dat', wave: 'x.345x|=.x', data: ['head', 'body', 'tail', 'data']},
  {name: 'req', wave: '0.1..0|1.0'},
  {name: 'ack', wave: '1.....|01.'}
]}
```

```
{signal: [
  {name: "Alfa", wave: "01.zx=ud.23.456789" },
  {name: 'clk', wave: 'p.....|P..'},
  {name: 'dat', wave: 'x.345x|=.x', data: ['head', 'body', 'tail', 'data']},
  {name: 'req', wave: '0.1..0|1.0'},
  {name: 'ack', wave: '1.....|01.'}
]}
```


### 信号分组

```json
{ signal: [
  {    name: 'clk',   wave: 'p..Pp..P'},
  ['Master',
    ['ctrl',
      {name: 'write', wave: '01.0....'},
      {name: 'read',  wave: '0...1..0'}
    ],
    {  name: 'addr',  wave: 'x3.x4..x', data: 'A1 A2'},
    {  name: 'wdata', wave: 'x3.x....', data: 'D1'   },
  ],
  ['Slave',
    ['ctrl',
      {name: 'ack',   wave: 'x01x0.1x'},
    ],
    {  name: 'rdata', wave: 'x.....4x', data: 'Q2'},
  ]
]}
```


### 周期与相位控制

DDR Read transaction时序图的代码

```json
{ signal: [
  { name: "CK",   wave: "P.......",                                              period: 2  },
  { name: "CMD",  wave: "x.3x=x4x=x=x=x=x", data: "RAS NOP CAS NOP NOP NOP NOP", phase: 0.5 },
  { name: "ADDR", wave: "x.=x..=x........", data: "ROW COL",                     phase: 0.5 },
  { name: "DQS",  wave: "z.......0.1010z." },
  { name: "DQ",   wave: "z.........5555z.", data: "D0 D1 D2 D3" }
]}
```


### 标题,脚注和缩放

```json
{signal: [
  {name:'clk',         wave: 'p....' },
  {name:'Data',        wave: 'x345x', data: 'a b c' },
  {name:'Request',     wave: '01..0' }
],
config: { hscale: 3},
 head:{
   text:'WaveDrom example',
   tick:0,
 },
 foot:{
   text:'Figure 100',
   tock:9
 },
}
```


### 带箭头

```json
{ signal: [
  { name: 'A', wave: '01........0....',  node: '.a........j' },
  { name: 'B', wave: '0.1.......0.1..',  node: '..b.......i' },
  { name: 'C', wave: '0..1....0...1..',  node: '...c....h..' },
  { name: 'D', wave: '0...1..0.....1.',  node: '....d..g...' },
  { name: 'E', wave: '0....10.......1',  node: '.....ef....' }
  ],
  edge: [
    'a~b t1', 'c-~a t2', 'c-~>d time 3', 'd~-e',
    'e~>f', 'f->g', 'g-~>h', 'h~>i some text', 'h~->j'
  ]
}
```



### 组合逻辑电路

```json
{ assign:[
  ["out",
    ["|",
      ["&", ["~", "a"], "b"],
      ["&", ["~", "b"], "a"]
    ]
  ]
]}
```



```json
{ assign:[
  ["out",
    ["XNOR",
      ["NAND",
        ["INV", "a"],
        ["NOR", "b", ["BUF","c"]]
      ],
      ["AND",
        ["XOR", "d", "e", ["OR","f","g"]],
        "h"
      ]
    ]
  ]
]}
```
