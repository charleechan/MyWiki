# Markdown支持绘制脑图啦
使用插件[gitbook-plugin-simple-mind-map](https://github.com/snowdreams1006/gitbook-plugin-simple-mind-map#readme)绘制脑图

* 代码块标识:`markdown`, 且代码块外要包一层壳,`{% simplemindmap style={"height":"600px"}%}`,`{% endsimplemindmap %}`

```
* simplemindmap
    * config book.json
        * plugins
            * others
            * simple-mind-map
        * pluginsConfig
            * others
            * simple-mind-map
                * type
                * preset
                * linkShape
                * autoFit
                * style
    * custom file.md
        * markdown
            * type
            * preset
            * linkShape
            * autoFit
            * style
        * txtmap
        * json
        * mindmup
```


对应的脑图为

{% simplemindmap style={"height":"600px"}%}
```markdown
* simplemindmap
    * config book.json
        * plugins
            * others
            * simple-mind-map
        * pluginsConfig
            * others
            * simple-mind-map
                * type
                * preset
                * linkShape
                * autoFit
                * style
    * custom file.md
        * markdown
            * type
            * preset
            * linkShape
            * autoFit
            * style
        * txtmap
        * json
        * mindmup
```
{% endsimplemindmap %}