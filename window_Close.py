# -*- coding: utf-8 -*-
"""
Function:定义了多种关闭窗口的函数，实现不同场合下的窗口关闭功能
1.imagebutton_leftclick： 通过image识别button位置，并实现左键单击button的功能，从而实现窗口关闭的功能
2. alt_f4_enter: 将窗口置于最上层，通过alt_f4＋enter快捷键实现窗口关闭功能
3.
Author: Sun Jia
Date： 2020.08.24
Version：V0.1
"""
import win32gui
import pyautogui
import time
def imagebutton_leftclick(image):
    try:
        button = pyautogui.locateOnScreen(image)
        print(button)
        assert button != None
        x, y = pyautogui.center(button)  # 获得中心点
        print(x, y)
        pyautogui.click(x, y)
    except AssertionError:
        print('未识别到图片所示按钮')

def alt_f4(window_name):
    try:
        hwnd_title = dict()
        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(get_all_hwnd, 0)
        assert window_name in hwnd_title.values()
        window_ID = list(hwnd_title.keys())[list(hwnd_title.values()).index(window_name)]
        print(window_ID)
        win32gui.SetForegroundWindow(window_ID)
        time.sleep(2)
        pyautogui.hotkey('altleft', 'f4')
    except AssertionError:
        print('窗口不存在')

def alt_f4_enter(window_name):
    try:
        hwnd_title = dict()
        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(get_all_hwnd, 0)
        assert window_name in hwnd_title.values()
        window_ID = list(hwnd_title.keys())[list(hwnd_title.values()).index(window_name)]
        print(window_ID)
        win32gui.SetForegroundWindow(window_ID)
        time.sleep(0.5)
        pyautogui.hotkey('altleft', 'f4')
        time.sleep( 0.5 )
        pyautogui.press('enter')
    except AssertionError:
        print('窗口不存在')


if __name__ == "__main__":
    imagebutton_leftclick('veri_cancel_button.PNG')
    alt_f4('Python 3.7.3 Shell')