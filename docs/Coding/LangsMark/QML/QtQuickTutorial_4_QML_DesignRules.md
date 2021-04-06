# Qt Quick开发教程4:设计规则与流程

## QML支持的函数:
1. Math.round(5*1.3),Qt.quit(),qsTr(“myButton”),console.log("hello"),Screen.width,
2. Image类中: 使用变量progress查询加载进度; 变量Image.status(值为ready表示图片已加载); 

## QML界面设计规则

一般顶层的Rectangle的ID为root;
.qmlproject可以设置QML文件,JS文件及图片文件的目录

QML 的**窗体**界面设计如下:
<div align="center"><img src="./assets/QMLDesignRules.jpg"></div>

下面对其中的内容进行详细介绍:
1. `Window :window`: 主窗体
   * 属性 `W:640 H:480`
   * 方法 `onCompleted`,`window`创建完成时会调用,如`window.showMaximized`.
2. `ScrollView:mainView`: 主窗体的视图格式,可以是`ScrollView`,`Stacked View`
   * 属性 `W:1.W H:1.H`
3. `Item:mainContent`:
   * 属性 `W:1.W H:6.H+7.H+200 `
4. `Item:leftMargin`:
   * 属性 `W:3.marginWidth`
5. `Item:rightMargin`:
   * 属性 `W:3.marginWidth`
6. `Text:header`:
   * 属性 `W:contentWidth,H:contentHeight,text,color,font,Anchors{top,bottom,horizontalCenter}`
7. `Column:mainLayout`:
   * 属性 `Anchors{top,topMargin,left,right},spacing`
   * 其他 `Grid:subLayout,spacing,columns`

## 常用的控件类及其属性、信号、方法等

* **Anchors** includes: `top`, `topMargin`, `horizontalCenter`
* **Text** includes:id, `text`, `anchors`, `font.pixelSize`, `horizontalAlignment`, `color`
* **TextInput** includes:`id`, `anchors`, `onAccepted`, `text`,`font.pixelSize`, `horizontalAlignment`, `color`
* **MouseArea** includes:`id`, `anchors`, `onClicked` `(,hoverEntered)(,onEntered)(,onExited)`
* **Rectangle** includes:`id`,`width`,`height`,`color(,x)(,y)(,anchors)(border.color)(border.width)(radius)(,Text)(,MouseArea)`
* **Image** includes:`id`,`source`,`sourceSize.height`,`sourceSize.width`,`anchors`,`onProgressChanged`,`onStatusChanged(,Text)(,MouseArea)`
* **AnimatedImage** includes:`id`,`source`,`(x),(y)`,`anchors`,`onProgressChanged`,`onStatusChanged(,Text)(,MouseArea)`
* **Flickable**(滚动条) includes:`id`,`width`,`height(滚动区域)`, `contentWidth`, `contentHeight(要滚动的内容)`, `contentY(当前显示内容相对于Flickable区域左上角的Y offset值), 垂直滚动的设置: Math.min(contentHeight-height, Math.max(0,player.y-height/2)))`, `boundsBehavior: Flickable.StopAtBounds`, `interactive: true`

> `Item`的所有子类: `AnimatedSprite`, `BorderImage`, `Canvas`, `Column`, `ColumnLayout`, `Flickable`, `Flipable`, `Flow`, `FocusScope`, `Grid`, `GridLayout`, `Image`, `Loader`, `MouseArea`, `MultiPointTouchArea`, `ParticlePainter`, `PathView`, `PinchArea`, `Rectangle`, `Repeater`, `Row`, `RowLayout`, `ShaderEffect`, `ShaderEffectSource`, `Shape`, `SignalSpy`, `SpriteSequence`, `StackLayout`, `TestCase`, `Text`, `TextEdit`, and `TextInput`.

## 自定义控件类

`自定义Item` includes: 先定义属性(`property bool/string/int/double [属性名]:初始值`),信号(`signal buttonClicked`,使用时直接`buttonClicked()`即触发信号), 再实例化内部需要的其他控件.

`使用自定义Item`: 控件类名(=自定义Item所在文件名){… 设置属性…,… 实现槽函数`onButtonClicked:{console.log(“I’m slot”)} }`

## 快速例化

`Repeater`类:包含一个`model`和一个`delegate`,`model`常为数值(例如`5`),`delegate`可以是任意Item类. `Repeater`一般被包含在`Row`,`Column`,`Grid`类的实例中，生成一行/列/框相类似的`Item`.

## 其他Trick

* 系统窗口的渐变色`gradient: Gradient{GradientStop{position:0.9;color:Qt.darker(palette.window, 1.8)}`
* `SystemPalette` 使用系统自带配色
* `Loader` 加载页面(`*.qml`),`Timer` 定时器,并行动画`ParallelAnimation`,顺序动画`SequentialAnimation`
* `XmlListModel`使用互联网API生成线性`Model`

(属性`title`和`pubDate`可直接被View访问)

```javascript
  import QtQuick 2.0
  import QtQuick.XmlListModel 2.0
  XmlListModel {
      id: xmlModel
      source: "http://www.mysite.com/feed.xml"
      query: "/rss/channel/item"
      XmlRole { name: "title"; query: "title/string()" }
      XmlRole { name: "pubDate"; query: "pubDate/string()" }
  }
```