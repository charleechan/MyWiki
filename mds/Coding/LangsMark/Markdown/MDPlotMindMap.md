# Markdown支持绘制脑图啦
使用插件`gitbook-plugin-simple-mind-map`绘制脑图

代码块标识:markdown

代码
````
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
````

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