import time
from pywinauto import application
import pyautogui
# 避免失控
pyautogui.FAILSAFE = True

# 默认延迟时间是0.1秒  这是个全局变量
pyautogui.PAUSE = 0.1

# app = application.Application().start('notepad.exe')
# app.Notepad.MenuSelect('帮助->关于记事本')
# time.sleep(.5)
# ABOUT = u'关于“记事本”'
# OK = u'确定'
# app[u'关于“记事本”'][u'确定'].Click()
#
# app.Notepad.TypeKeys(u"杨彦星")
#
# dialogs = app.windows_()
# app.Notepad.MenuSelect("文件->退出")
# time.sleep(2)
# app[u'记事本'][u'不保存'].Click()


dirs = u"D:\网易云音乐\CloudMusic\cloudmusic.exe"   #应用所在路径
app = application.Application()
app.start(dirs)

pyautogui.hotkey('ctrl', 'p')
