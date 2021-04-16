# 建立自己的QML Style Sheet文件

可以通过建立自定义的`Style Sheet`文件,来管理各个不同页面(QML)的风格.

具体方法是,
1. 在要定义样式的QML脚本中使用`pragma Singleton`,声明这是一个单例文件.
2. 将该样式的组件定义为单例;
3. 导入到要使用的QML界面中.

下面是一个实例.
## 声明一个单例的样式QML脚本文件

```javascript
//MyStyleObject.qml
pragma Singleton 
import QtQuick 2.0  
  
Item {  
    readonly property string colourBlue: "blue"  
    readonly property string colourRed: "red"  
    readonly property int fontPointSize: 16  
}  
```

## 注册单例组件

两个方法:在C++代码中注册;或者使用`qmldir`文件注册.本着前后端尽量分离的原则,建议使用第二种.

第一个方法:
```cpp
#include <QtQml>  
...  
qmlRegisterSingletonType( QUrl("file:///absolute/path/MyStyleObject.qml"), "ca.imaginativethinking.tutorial.style", 1, 0, "MyStyle" );  
...  
```

第二个方法:**在`MyStyleObject.qml`所在目录添加一个`qmldir`文件**:

> 当`import`一个目录时,QML Engine会首先查找`qmldir`文件,并根据该目录导入相应的脚本文件.

如果目录结构如下所示:

```
/root
  + absolute
  |  + path
  |  |  + qmldir
  |  |  + MyStyleObject.qml
  |  |  + AnotherObject.qml
  |  |  + MyButton.qml
  |  |  + MySwitch.qml
  |  + main.qml
```

相应的`qmldir`文件的内容:

```
singleton MyStyle 1.0 MyStyleObject.qml  
MyOtherObject 1.0 AnotherObject.qml  
MyButton 1.0 MyButton.qml  
```

> 注意,虽然`qmldir`中没写`MySwitch.qml`,但仍然会按默认的设置进行导入.


## 导入并使用单例

如果使用C++注册的方法,则需要在`QML`脚本中导入`qmlRegisterSingletonType`函数的第2个形参(**包名**).

如果使用`qmldir`的方法,只需要导入该目录即可

```javascript
import QtQuick 2.0  
import "path"  
  
Rectangle {  
    anchors.fill: parent  
    color: MyStyle.colourBlue // <-- Notice that to access the singleton I use the object name not id (i.e. Capital M)  
}  
```

> 注意:即使`main.qml`在此`path`目录中,你仍然需要导入该目录`import "path"  `,因为自动导入系统中不会读取`qmldir`.