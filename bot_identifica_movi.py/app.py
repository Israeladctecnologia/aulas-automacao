import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(881,575,(0,152,0)):
        pyautogui.press('a')
        sleep(0.01)
    if pyautogui.pixelMatchesColor(947,575,(255,0,0)):
        pyautogui.press('s')
        sleep(0.01)
    if pyautogui.pixelMatchesColor(1015,576,(244,244,2)):
        pyautogui.press('j')
        sleep(0.01)
