import pyautogui, time, pyperclip, webbrowser



#1) Navegue até o site https://cursoautomacao.netlify.app/
pyautogui.hotkey('winleft', 'down')

time.sleep(2)
webbrowser.open_new('https://cursoautomacao.netlify.app/')

time.sleep(1)
pyautogui.click(x=1120,y=309 ,duration=0.1)
time.sleep(1)
pyautogui.hotkey('winleft', 'up')

#2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome

time.sleep(2)
pyautogui.scroll(-3300)

time.sleep(2)
pyautogui.click(441,545, duration=2)
pyautogui.typewrite('Israel Alexsander D Candido')

for i in range(4):
    time.sleep(2)
    pyautogui.click(1356,318)

time.sleep(2)
pyautogui.click(1090,522)
pyautogui.typewrite('Israel Alexsander D Candido')

#3) Clique em alerta, para gerar a alerta
time.sleep(2)
pyautogui.click(1137,558)

#4) Feche a alerta
time.sleep(2)
pyautogui.click(742,193)

#5) Suba a página totalmente para cima
time.sleep(3)
pyautogui.hotkey('pageUp')

#) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
time.sleep(3)
pyautogui.scroll(-2000)

pyautogui.click(385,368, duration=2)
pyautogui.click(221,375, duration=2)

#7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='Você terminou!', title='Terminou', button='o')









