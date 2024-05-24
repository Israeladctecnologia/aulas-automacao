import pyautogui, time, pyperclip, webbrowser

def sair():
    pyautogui.click(104,389, duration=2)
    pyautogui.click(65,690, duration=2)
    pyautogui.click(66,634, duration=2)
while True:
    #Abrti página do Instagram
    webbrowser.open('https://www.instagram.com/')
    time.sleep(2)
    pyautogui.hotkey('winleft', 'up')

    #Entrar com usuário
    pyautogui.click(795,320, duration=2)
    pyautogui.typewrite('israeladctecnologia@gmail.com')

    #Entrar com Senha
    time.sleep(1)
    pyautogui.click(785,365, duration=0.1)
    pyautogui.typewrite('08022021Gi@')

    #Clicar entrar
    time.sleep(1)
    pyautogui.click(860,415, duration=0.1)

    #Não lembrar senha
    time.sleep(5)
    pyautogui.click(786,474, duration=0.1)

    #Pesquisar nike
    time.sleep(3)
    pyautogui.click(96,305, duration=2)
    time.sleep(2)
    pyautogui.click(125,233, duration=2)
    pyautogui.typewrite('nike')
    time.sleep(4)
    pyautogui.move(0, 50)
    time.sleep(3)
    pyautogui.click()
    '''
    #Rolar a pagiana
    time.sleep(2)
    pyautogui.scroll(-500)
    '''

    #Clicar post mais recente
    time.sleep(2)
    pyautogui.click(522,665, duration=2)

    #verificar se curtida
    time.sleep(5)
    like = pyautogui.locateCenterOnScreen('image.png')
    try:
       like = pyautogui.screenshot('/aulas-automacao/bot_Instgram/image.png')
    except FileNotFoundError as e:
        print(f"Erro: {e}")

    if like is not None:
        sair()
        time.sleep(10)
    elif like is None:
        pyautogui.click(675,572, duration=2)
        time.sleep(5)
        
        pyautogui.click(714,573, duration=2)
        time.sleep(2)
        
        pyautogui.click(729,672, duration=2)
        time.sleep(2)
        pyautogui.typewrite('Top!')
        pyautogui.press('enter')
        sair()
        time.sleep(10)

