import pyautogui
import pyperclip

def escr_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

pyautogui.moveTo(x=1000, y=340, duration=1)
pyautogui.click()
escr_frase('Boa Noite!')