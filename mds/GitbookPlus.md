## Gitbook 插件

Gitbook 插件是扩展 GitBook 功能(电子书和网站)的最佳方式.

只要是 Gitbook 默认没有提供的功能,基于插件机制都可以自行扩展,是插件让 Gitbook 变得更加强大.

Gitbook官网已经停止对插件的维护,目前只可以在 `npmjs` 官网搜索 `gitbook-plugin-<name>` 插件.

## 安装Gitbook 插件

### 方法1 
一旦你找到你想要安装的插件,你需要将它添加到你的 book.json 配置文件,如果没有该文件则自行创建.

```json
{
    "plugins": ["myPlugin", "anotherPlugin"]
}
```

您还可以使用以下命令指定特定版本: `myPlugin@0.3.1` .
默认不填写版本的情况下,GitBook 使用**最新版本(兼容版本)**的插件.

如果是官网在线环境,网站会自动帮你安装插件.
如果是在本地环境,直接运行 `gitbook install` 来安装插件.

```bash
$ gitbook install
```
### 方法2

使用 npm 提前下载插件再安装到本地项目:

```bash
$ npm install gitbook-plugin-<name>
$ gitbook install
```

## 开发插件

`GitBook` 插件是在 `npm` 上发布的遵循传统定义的 `node` 包,除了标准的 `node` 规范外还有一些 `Gitbook` 自身定义的相关规范.

1. 目录结构
`Gitbook` 插件最基本的项目结构至少包括配置文件 `package.json` 和入口文件 `index.js` ,其他目录文件根据插件用途自行增减.

```
.
├── index.js
└── package.json
```

实际插件项目略有不同,可能还会有 `_layouts` 布局目录, `asset` 资源目录以及自定义 `example` 示例目录和 `docs` 文档目录等等.

2. `package.json`

`package.json` 是**nodejs**的配置文件,`Gitbook` 插件同样遵循该规范,配置文件声明了插件的版本描述性信息,除此之外还有 `Gitbook` 相关字段,遵循`schema`准则,基本示例如下:

```json
{
    "name": "gitbook-plugin-mytest",
    "version": "0.0.1",
    "description": "This is my first GitBook plugin",
    "engines": {
        "gitbook": ">1.x.x"
    },
    "gitbook": {
        "properties": {
            "myConfigKey": {
                "type": "string",
                "default": "it's the default value",
                "description": "It defines my awesome config!"
            }
        }
    }
}
```

值得注意的是,包名称必须以 `gitbook-plugin-`开头，包引擎应该包含`gitbook`.如需了解 `package.json` 的规范,可参考[官方文档](https://docs.npmjs.com/files/package.json).

3. `index.js`
`index.js` 是插件运行时的入口,基本示例如下:

```
module.exports = {
    // 钩子函数
    hooks: {},

    // 代码块
    blocks: {},

    // 过滤器
    filters: {}
};
```

## 发布插件
`GitBook` 插件可以在`npmjs`官网上发布.

如需发布插件,首先需要在`npmjs`官网上注册帐户,然后通过命令行发布.
```bash
$ npm publish
```

## 专用插件
专用插件可以托管在 `GitHub` 上,并使用 `git urls`:
```json
{
    "plugins": [
        "myplugin@git+https://github.com/MyCompany/mygitbookplugin.git#1.0.0"
    ]
}
```

### 本地测试插件
使用 `npm link` 可以在发布之前测试你的插件,命令详情参考[官方文档](https://docs.npmjs.com/cli/link)

在插件的文件夹中,运行：

```bash
$ npm link
```

然后在您的书或者文档的文件夹中执行:

```bash
$ npm link gitbook-plugin-<name>
```
单元测试插件
`gitbook-tester`可以方便地为你的插件编写`Node.js/Mocha`单元测试.
