#! /usr/bin/env python

from pywinauto import application
from pykeyboard import PyKeyboard
import time

class Pywin(object):
    """
    tool_name : 程序名称，支持带路径
    windows_name : 窗口名字
    """
    SLEEP_TIME = 1

    def __init__(self):
        """
        初始化方法，初始化一个app
        """
        self.app = application.Application()

    def run(self, tool_name):
        """
        启动应用程序
        """
        self.app.start(tool_name)
        time.sleep(3)

        # 作用到主窗口
        self.app.window_(found_index=0)

        k = PyKeyboard()
        # k.press_key(k.enter_key)
        k.press_key(k.function_keys[5])

        time.sleep(2)

        # 热键关闭网易云
        k.press_keys([k.alt_key, k.function_keys[4]])

    def connect(self, window_name):
        """
        连接应用程序
        app.connect_(path = r"c:\windows\system32\notepad.exe")
        app.connect_(process = 2341)
        app.connect_(handle = 0x010f0c)
        """
        self.app.connect(title = window_name)
        time.sleep(1)

    def close(self, window_name):
        """
        关闭应用程序
        """
        self.app[window_name].Close()
        time.sleep(1)

    def max_window(self, window_name):
        """
        最大化窗口
        """
        self.app[window_name].Maximize()
        time.sleep(1)

    def menu_click(self, window_name, menulist):
        """
        菜单点击
        """
        self.app[window_name].MenuSelect(menulist)
        time.sleep(1)

    def input(self, window_name, controller, content):
        """
        输入内容
        """
        self.app[window_name][controller].TypeKeys(content)
        time.sleep(1)

    def click(self, window_name, controller):
        """
        鼠标左键点击
        example:
        下面两个功能相同,下面支持正则表达式
        app[u'关于“记事本”'][u'确定'].Click()
        app.window_(title_re = u'关于“记事本”').window_(title_re = u'确定').Click()
        """
        self.app[window_name][controller].Click()
        time.sleep(1)

    def double_click(self, window_name, controller, x = 0,y = 0):
        """
        鼠标左键点击(双击)
        """
        self.app[window_name][controller].DoubleClick(button = "left", pressed = "",  coords = (x, y))
        time.sleep(1)

    def right_click(self, window_name, controller, order):
        """
        鼠标右键点击，下移进行菜单选择
        window_name : 窗口名
        controller：区域名
        order ： 数字，第几个命令
        """
        self.app[window_name][controller].RightClick()
        k = PyKeyboard()
        for down in range(order):
            k.press_key(k.down_key)
            time.sleep(0.5)
        k.press_key(k.enter_key)
        time.sleep(1)

if __name__ ==  "__main__":
    app = Pywin()
    
    # 网易云音乐例子
    tool_name = "D:\网易云音乐\CloudMusic\cloudmusic.exe"
    
    # 启动程序
    app.run(tool_name)





