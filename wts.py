import pyautogui
import pyperclip
import time

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.click(1191,682, duration=1)
time.sleep(1)
escrever_frase('Amo te! Lindona sz')
time.sleep(1)
pyautogui.press('enter')
