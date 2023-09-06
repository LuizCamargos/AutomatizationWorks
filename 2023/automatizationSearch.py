import pyautogui
# from datetime import datetime
import time
from random import randint

listaPergunta=[
'Um Sonho de Liberdade(1994)',
'O Poderoso Chefão(1972)',
'O Poderoso Chefão II(1974)',
'Batman: O Cavaleiro das Trevas(2008)',
'A Lista de Schindler(1993)',
'12 Homens e uma Sentença(1957)',
'Pulp Fiction: Tempo de Violência(1994)',
'O Senhor dos Anéis: O Retorno do Rei(2003)',
'Três Homens em Conflito(1966)',
'Clube da Luta(1999)'
]

time.sleep(3)
pergunta = listaPergunta[randint(0,len(listaPergunta))]
# pyautogui.write(pergunta, interval=.1)
# pyautogui.press(['enter'])
pyautogui.hotkey(['ctrl', 'e'],interval=.1)

print(pergunta)

#pegar ponteiro
# pyautogui.moveTo(x=100, y=100, duration=3,tween=(pyautogui.easeInOutQuad) )

# Get time
# time = datetime.now().time()