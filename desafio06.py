import pyautogui
import time
import pyperclip


def colar_email(email):
    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'v')

def colar_senha(senha):
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'v')

email = pyautogui.prompt(text='Digite seu email: ', title='Email')
print(email)
senha = pyautogui.password(text='Digite sua senha:', title='Senha', mask='*')
print(senha)

pyautogui.click(785,136, duration=1)

colar_email(email)
pyautogui.press('enter')
colar_senha(senha)