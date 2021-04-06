# Qt Quick开发教程5:动画

## 第一种-`Behavior on property`

第1种动画实现的方式
* Behavior on property:当属性的值发生变化时,将会触发下面的动作

```javascript
Behavior on scale{
  NumberAnimation{
    //持续800ms
    duration: 800
    easing.type:Easing.OutBounce
  }
}
```

## 第二种 动画实现的方式
* `PropertyAnimation`是用来为属性提供动画的最基本的动画元素，可以用来为 `real` 、 `int` 、 `color` 、 `rect` 、 `point` 、 `size` 和 `vector3d` 等属性设置动画，
* `NumberAnimation` `、colorAnimation` 、 `RotationAnimation` 和 `Vector3dAnimation` 等元素继承。
* `NumberAnimation` 对 `real` 和 `int` 属性提供了更高效的实现；
* `Vector3dAnimation` 对 `vector3d` 属性提供了更高效的支持；
* `ColorAnimation` 和 `RotationAnimation` 分别对 `color` 和 `rotation` 属性变化动画提供了特定的属性支持。
* 在需要触发时进行 `scaleAnimation.start()` 即可

```javascript
    PropertyAnimation{
        id:scaleAnimation
        target: imageOfElement
        property: "scale"
        from:0
        to:1
        duration: 1000
        easing.type: Easing.OutBack
    }

    //NumberAnimation修改某属性的数值
    NumberAnimation{
        id:opacityAnimation
        target: imageOfElement
        property: "opacity"
        from:0
        to:1
        duration: 2800
        easing.type: Easing.OutBack

    }
```

## 第三种 使用状态机分别写状态和跳转
* `State` 中实现 `AnchorChanges` , `PropertyChanges` 等的赋值
* `Transition` 中实现状态跳转时发生的动画,如果只有一 `State`,则只有一个 `Transition`
* 跳转条件:在需要触发处对`rect2.state`赋值即可

```javascript
Rectangle{
id: rect2
width: Screen.width/2
height: Screen.height/12
color:"transparent"
radius: 20
states: [
  State {
  name: "ENTERED"
      PropertyChanges {
        target: rect2
        color:"orange"
      }
  },
  State {
    name: "EXITED"
    PropertyChanges {
      target: rect2
      color:"transparent"
    }
  }
]
transitions: [
  Transition {
    from: "EXITED"
    to: "ENTERED"
    ColorAnimation {target:rect2;duration: 1200}
  },
  Transition {
    from: "ENTERED"
    to: "EXITED"
    ColorAnimation{ target: rect2; duration:1200}
  }
]
}

```