import pyautogui
import time
'''
    # Essa Forma seleciona e arrasta todos os itens de uma vez
pyautogui.moveTo(x=1320, y=266, duration=1)
pyautogui.dragTo(x=896, y=123, button='left', duration=1)
pyautogui.dragTo(x=910, y=565, button='left', duration=1)
'''
for i in range(10):
    pyautogui.moveTo(900,139, duration=1)
    pyautogui.dragTo(899,515, button='left', duration=0.5)


