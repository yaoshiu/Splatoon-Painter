# SplatoonPainter - 电子刺绣师

![image-20221006215738083](https://s2.loli.net/2022/10/06/YVWb4lqAmzvex5U.png)

一个在Linux系统上模拟Switch Pro控制器自动在斯普拉遁3涂鸦图片的脚本。

## 背景

起初是在jump上看到了利用单片机烧录自动绘画的程序，然而手头并没有单片机。于是便有了“既然带蓝牙的单片机能搞定的事情为什么带蓝牙的个人电脑搞不定呢？”的想法。

## 安装

在Linux系统上通过`git clone`将本仓库克隆到本地后通过`pip`安装

````
git clone https://github.com/yaoshiu/Splatoon-Painter.git
cd Splatoon-Painter
sudo pip install .
````

## 使用说明

请确保在Linux环境下以su权限运行，且图像为黑白.bmp位图

```
usage: main.py [-h] [-r RECONNECT] filename



positional arguments:

  filename              The file address of the .bmp file to be input



options:

  -h, --help            show this help message and exit

  -r RECONNECT, --reconnect RECONNECT

                        If the switch has already been paired.
```

在成功连接并弹出第一次提示后请打开Nintendo Switch上的Splatoon涂鸦页面，并且将画笔调至最小然后至于左上角

## 示例

如果你是第一次配对Nintendo Switch，请使用如下的指令

```
sudo main.py my_picture.bmp
```

如果在先前已经运行过该程序并成功配对过Nintendo Switch，请使用如下指令

```
sudo main.py -r my_picture.bmp
```

## 相关仓库

感谢 [Brikwerk/nxbt](https://github.com/Brikwerk/nxbt) 提供的控制器 API

## 使用许可

MIT © Phie Ash