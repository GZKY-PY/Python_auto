import pyautogui

# 避免失控
pyautogui.FAILSAFE = True

# 默认延迟时间是0.1秒。
pyautogui.PAUSE = 0.1

# 热键 组合键
pyautogui.hotkey('winleft', 'r')

# 输入命令
pyautogui.typewrite(message='cmd',interval=0.1)
pyautogui.press('enter')

pyautogui.typewrite(message='cd Desktop/auto_cmd/',interval=0.1)
pyautogui.press('enter')

# pyautogui.typewrite(message='"Shortcut to one.atmx.lnk"',interval=0.1)
# pyautogui.press('enter')

# 截图
im1 = pyautogui.screenshot()
im1.save('my_screenshot.png')

# 提示
pyautogui.alert(text='This is an alert box.', title='Test')

pyautogui.typewrite(message='exit',interval=0.1)
pyautogui.press('enter')



# demo
'''
#模拟输入信息
pyautogui.typewrite(message='Hello world!',interval=0.5)

#点击ESC
pyautogui.press('esc')

# 按住shift键
pyautogui.keyDown('shift')

# 放开shift键
pyautogui.keyUp('shift')

# 模拟组合热键
pyautogui.hotkey('ctrl', 'c')

'''
