# Splatoon Painter - 电子刺绣师

A script that simulates the Switch Pro controller on a Linux system to automatically paint pictures in Splatoon 3.

一个在Linux系统上模拟Switch Pro控制器自动在斯普拉遁3涂鸦图片的脚本。

## Background

At first, I saw a program on Jump App that uses a microcontroller to burn automatic painting, but I didn't have a microcontroller at hand. So I thought, "If a microcontroller with Bluetooth can do it, why can't a PC with Bluetooth do it?"

## Installation

Clone the repository locally with `git clone` and install it with `pip` on a Linux system

````
sudo pip install .
````

## Usage

Make sure to run with su privileges in a Linux environment

```
usage: main.py [-h] [-r RECONNECT] filename



positional arguments:

  filename The file address of the .bmp file to be input



options:

  -h, --help show this help message and exit

  -r RECONNECT, --reconnect RECONNECT

                        If the switch has already been paired.
```

## Example

If you are pairing a Nintendo Switch for the first time, use the following command

```
sudo main.py my_picture.bmp
```

If you have previously run the program and successfully paired a Nintendo Switch, use the following command

```
sudo main.py -r my_picture.bmp
```

## Related efforts

Thanks to [Brikwerk/nxbt](https://github.com/Brikwerk/nxbt) for the controller API

## License

MIT