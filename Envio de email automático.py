import pyautogui as py
import pyperclip
from time import sleep

# Comunicado de alerta da inicialização do código e pausa entre os comandos para o programa fluir da forma adequada
py.alert(text='O programa irá iniciar, não mexa no computador enquanto o programa estiver em andamento. ', title='ATENÇÃO', button='OK')
py.PAUSE=1.5

#Entrando no navegador
py.press('win')
py.write('chrome')
py.press('enter')

#Copiando link do outlook
pyperclip.copy('https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1653265966&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f0%2f%3fstate%3d1%26redirectTo%3daHR0cHM6Ly9vdXRsb29rLmxpdmUuY29tL21haWwvMC8%26RpsCsrfState%3d9987d8fd-19cb-a995-f86f-284e5f345b92&id=292841&aadredir=1&whr=hotmail.com&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015')

#Colando na barra de navegação
py.hotkey('ctrl','v')
py.press('enter')
sleep(4)

#Observação importante: o email e a senha já estão salvos no desktop, basta apenas clicar em 'Seguinte' e em seguida 'Iniciar sessão'
py.click(x=784, y=456)
sleep(4)
py.click(x=796, y=498)
sleep(4)
py.click(x=140, y=131)
sleep(4)
py.click(x=157, y=197)
sleep(4)

#Email do destinatário
pyperclip.copy('ju_silva25@icloud.com')
py.hotkey('ctrl','v')
py.click(x=89, y=258)
sleep(2)

# Assunto do email
pyperclip.copy('RELATÓRIO')
py.hotkey('ctrl','v')
py.click(x=77, y=314)
sleep(2)

# Texto do email
pyperclip.copy(''' Segue o relatório abaixo 


Atenciosamente,

Júlia ''')
py.hotkey('ctrl','v')
py.click(x=93, y=644)

# Comunicado de finalização da automoção
py.alert(text='O programa foi finalizado com sucesso, use seu desktop normalmente. ', title='COMUNICADO', button='OK')
