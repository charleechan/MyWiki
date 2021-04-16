# Qt Quick开发教程3:导出C++到QML

元对象系统(Meta-Object System)：只要一个CPP类进入了元对象系统，类的方法和属性就可以在QML中访问。



### 1 导出 **类** 到QML

要导出的类需要有以下这种形式：

```CPP
class QQuickText : public QQuickImplicitSizeItem    //必须继承自QObject类或QObject派生类
{    
    Q_OBJECT    //必须使用Q_OBJECT宏
    Q_PROPERTY(type name READ getFunction WRITE setFunction RESET resetFunction NOTIFY notifySignal)
    Q_PROPERTY(QString text READ text WRITE setText NOTIFY textChanged) 
    /*定义元对象系统可访问的属性,定义了一个类型为QString的名为text的属性, 通过text()和setText()进行访问和赋值,当text的内容改变,用户要触发textChanged信号,以通知QML该属性已改变*/
    Q_PROPERTY(QFont font READ font WRITE setFont NOTIFY fontChanged)
    //...

public:
    QQuickText(QQuickItem *parent=0);
    ~QQuickText();//构造函数与析构函数
    enum HAlignment { AlignLeft = Qt::AlignLeft,
                       AlignRight = Qt::AlignRight,
                       AlignHCenter = Qt::AlignHCenter,
                       AlignJustify = Qt::AlignJustify };
    Q_ENUM(HAlignment)
    //定义元对象系统可访问的枚举类型

    QString m_text;

    //text()和setText()不能被QML访问
    QString text() const{
        return m_text;
    }
    void setText(const QString & text)
    {
        m_text = text;
        emit textChanged();
    }

    //...
    //doLayout()可被QML访问
    Q_INVOKABLE void doLayout(); // ### Qt 6: remove

//所有signals均可以被QML访问
signals:
    //...
//所有slots均可以被QML访问
slots:
    //...

}

```
类实现完成之后，一般在`main.cpp`里进行注册
```cpp
//qmlRegisterType<ClassName>("uri",1,0,"qmlName");
qmlRegisterType<ClassName>("PackageName",1,0,"qmlName");
```

要在QML中使用，还需要再QML文件中导入：
```javascript
import PackageName 1.0

Rectangle{
    width:360
    height:360
    qmlName{
        id:...
        //PropertyName:
        text:...
    }    
}
```

### 2 导出 **对象/变量** 到QML

以下是将Cpp中名为`objectName2`的对象/变量导出到QML中`objectName1`的步骤：

> 1 注册属性:

在`main.cpp`中`engine.load...`之前添加一句:
```CPP
engine.rootContext()->setContextProperty("objectName1",objectName2);
```

> 2 使用属性：

导出的属性可以直接使用，与属性关联的对象，它的信号，槽，可调用方法，属性均可以在QML使用。


## 导出QML到C++

要在C++中使用QML,

```javascript
import QtQuick 2.2
import QtQuick.Controls 1.2
import QtQuick.Window 2.1

Window{
    obejectName: "rootObject"
    width: 360
    height: 360
    visible: true
    
    Text{
        objectName: "textLabel"
        text: "Hello World"
        anchors.centerIn: parent
        font.pixelSize: 26
    }
    
    Button{
        anchors.right: parent.right
        anchors.rightMargin: 4
        anchors.bottom: parent.bottom
        anchors.bottomMargin: 4
        text: "exit"
        objectName: "quitButton"
    }
}
```

在Cpp中将通过对象名objectName来访问其属性。

要访问该页面的rootObject及其他Object，一般在main.cpp中实现：
```cpp
//Step1: 找rootObject
QObject *root = NULL;
QList<QObject*> rootObjects = engine.rootObjects();
int count = rootObjects.size();
for(int i=0;i<count;i++)
{
    if(rootObjects.at(i)->objectName() == "rootObject")
    {
        root = rootObjects.at(i);
        break;
    }
}

//Step2: 找object
QObject *quitButton = root->findChild<QObject*>("quitButton");
//Step3: Process
if(quitButton)
{
    QObject::connect(quitButton, SIGNAL(clicked(),&app,SLOT(quit())));
}

//Step2: 找Object
QObject *textLabel = root->findChild<QObject*>("textLabel");
//Step3: Process
if(textLabel)
{
    textLabel->setProperty("color", QColor::fromRgb(255,0,0));
    bool bRet = QMetaObject::invokeMethod(textLabel,"doLayout");
}
```