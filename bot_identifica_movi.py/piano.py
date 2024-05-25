import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(1052,512, duration=1)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    sleep(0.02)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(977,502,(0,0,0)):
      click(977,502)
    if pyautogui.pixelMatchesColor(1047,503,(0,0,0)):
      click(1047,503)
    if pyautogui.pixelMatchesColor(1111,501,(0,0,0)):
      click(1111,501)
    if pyautogui.pixelMatchesColor(1130,510,(0,0,0)):
      click(1130,510)
