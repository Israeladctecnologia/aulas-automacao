import pyautogui
import pyperclip
import time

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')
time.sleep(1)
pyautogui.click(834,669, duration=1)
time.sleep(1)
escrever_frase('Como vai você?')
time.sleep(1)
pyautogui.press('tab')
time.sleep(1)
pyautogui.press('enter')