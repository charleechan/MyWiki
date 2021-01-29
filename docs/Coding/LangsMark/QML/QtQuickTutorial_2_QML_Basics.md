# Qt Quick开发教程2:QML语法

```xml
// 下面是导入语句
import QtQuick 2.9
import QtQuick.Window 2.2

/* QML文档可以看做是一个QML对象树,这里创建了Window根对象
和它的子对象Text */
Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Text {
        id: text1
        text: qsTr("hello QML!")
    }
}
```

## import语句
* 使用QML需要导入QtQuick模块。
* 如果需要使用Window，则还要导入QtQuick.Window 模块
* 版本号指示了本代码使用的Qt模块版本，Qt模块的版本是向下兼容的。

## QML数据类型
* 基本类型

  `int`,`string`等你熟悉的类型和QML模块自带的基本类型如`date`,`point`,`rect`,`size`等类型。
* QML对象类型
  定义一个对象：`类型名称{对象特性}`。对象中可以包含其他对象。如，上面代码中Window对象中包含了一个Text对象。
* JavaScript类型

  QML支持JavaScript对象和数组，可以通过var 类型创建并存储任何标准的JavaScript类型。

  ```xml
  import QtQuick 2.0

  Item {
      property var theArray: []
      property var theDate: new Date()

      Component.onCompleted: {
          for (var i = 0; i < 10; i++)
              theArray.push("Item " + i)
          console.log("There are", theArray.length, "items in the array")
          console.log("The time is", theDate.toUTCString())
      }
  }
  ```

## 属性
每个对象可以有一或多个属性。

`属性:值`的写法可以给属性赋值，可以是静态值，也可以是表达式。

每个属性的值可以使用本对象的值计算，也可用其他对象的值参与计算

注意，每个对象都有一个id，你可以理解为一个对象的id是它特殊的属性。例如前面代码中Text 对象的 id 为 text1，所以可以在其他对象中通过 `text1.text` 来获取 `Text` 对象中的 `text` 属性的值,但无法通过`text1.id` 来获取 `id` 的值。

## 注释
注释的写法与C++相似。
* 单行注释：`//`
* 多行注释：`/`和`/`

## 布局
QML的主要功能是用来布局的，它将替代ui_mainwindow.ui进行UI的渲染。

### anchors: 将对象锚定

anchors是一种对象的类。它可用的属性有：

|属性|值的类型|举例|
|:-:|:-:|:-:|
|anchors.top | AnchorLine |obj1.bottom - 将其的top与对象obj1的bottom锚定在一起|
|anchors.bottom | AnchorLine | obj1.bottom - 将其的top与对象obj1的bottom锚定在一起|
|anchors.left | AnchorLine | obj1.left - 将其的left与对象obj1的left锚定在一起|
|anchors.right | AnchorLine | obj1.left - 将其的right与对象obj1的left锚定在一起|
|anchors.horizontalCenter | AnchorLine | obj1.horizontalCenter - 将其的horizontalCenter与对象obj1的horizontalCenter锚定在一起|
|anchors.verticalCenter | AnchorLine | obj1.horizontalCenter - 将其的verticalCenter与对象obj1的verticalCenter锚定在一起|
|anchors.baseline | AnchorLine |
|anchors.fill | Item | parent - 将其父对象填充 |
|anchors.centerIn | Item | parent - 表示在其父对象的中心|
|anchors.margins | real |
|anchors.topMargin | real |
|anchors.bottomMargin | real |
|anchors.leftMargin | real |
|anchors.rightMargin | real |
|anchors.horizontalCenterOffset | real |
|anchors.verticalCenterOffset | real |
|anchors.baselineOffset | real |
|anchors.alignWhenCentered | bool |

## 测试
```xml
import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")

    Text {
        id: text1
        anchors.centerIn: parent
        text: qsTr("Hello Android")

        font.bold: true
        font { pointSize: 14; capitalization: Font.AllUppercase }

        Behavior on rotation {
            NumberAnimation { duration: 500 }
        }
    }

    Rectangle {
        id: colorRect
        width: 20 * 2
        height: width
        radius: 20
        border.color: "green"

        anchors.left: text1.right
        anchors.leftMargin: 10
        anchors.verticalCenter: text1.verticalCenter

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.debug("colorRect: ", parent.border.color)
                text1.rotation += 360
                text1.color = parent.border.color
            }
        }

        Rectangle {
            width: 12 * 2
            height: width
            radius: 12
            color: parent.border.color
            anchors.centerIn: parent
        }
    }

}
```
测试一下上述代码的效果。

## 添加图片

在源码目录放置文件夹`images`，将图片放置其中。在qml.qrc上右键选择`Open in Editor`，添加资源。

然后在qml文件中添加以下代码：

```xml
Image {
    id: backImg
    source: "images/bg1.png"
    width: parent.width
    anchors.bottom: parent.bottom
    fillMode: Image.PreserveAspectFit //缩放时保留宽高比
}
```

## 自定义对象类型
在项目里右键`/`，添加新文件，选择Qt类，然后选择QML File。文件名为`ColorText`。
然后将下列代码拷贝进去。
```xml
import QtQuick 2.9

Item {
    id: root
    Text {
        id: text1
        anchors.centerIn: parent
        text: qsTr("Hello Android")

        font.bold: true
        font { pointSize: 14; capitalization: Font.AllUppercase }

        Behavior on rotation {
            NumberAnimation { duration: 500 }
        }
    }

    Rectangle {
        id: colorRect
        width: 20 * 2
        height: width
        radius: 20
        border.color: "green"

        anchors.left: text1.right
        anchors.leftMargin: 10
        anchors.verticalCenter: text1.verticalCenter

        MouseArea {
            anchors.fill: parent
            onClicked: {
                console.debug("colorRect: ", parent.border.color)
                text1.rotation += 360
                text1.color = parent.border.color
            }
            hoverEnabled: true
            onEntered: {
                parent.width = 32
                parent.color = "black"
            }
            onExited: {
                parent.width = 40
                parent.color = "white"
            }
        }

        Rectangle {
            width: 12 * 2
            height: width
            radius: 12
            color: parent.border.color
            anchors.centerIn: parent
        }
    }
}
```

在main.qml中添加以下代码：

```xml
import QtQuick 2.9
import QtQuick.Window 2.2

Window {
    visible: true
    width: 640
    height: 480
    title: qsTr("Hello World")
    ColorText {
        anchors.centerIn: parent
    }
}
```
