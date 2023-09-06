from selenium import webdriver
import pyautogui
import time
from datetime import datetime
sistemaAntiBug = 0


def desligarLab1():
    print("Desligando Lab1")
    pyautogui.FAILSAFE = False

    print("Completado com sucesso!!")


def reiniciarTV():
    pyautogui.FAILSAFE = False

    senha = "master"
    ip = "10.40.22.240"

    pyautogui.click(x=1365, y=767, duration=0.5)
    pyautogui.click(x=0, y=767, duration=0.5)
    pyautogui.click(x=376, y=670, duration=0.5)
    pyautogui.click(x=717, y=175, duration=0.5)
    pyautogui.press('delete')
    pyautogui.typewrite(ip)
    time.sleep(3)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.click(x=670, y=317, duration=0.5)
    pyautogui.typewrite(senha)
    pyautogui.press("enter")
    time.sleep(3)
    pyautogui.mouseDown(x=576, y=20)
    time.sleep(1)
    pyautogui.mouseUp(x=0, y=27)
    pyautogui.click(x=13, y=43, duration=0.5)

    pyautogui.click(x=674, y=687, duration=0.5)
    pyautogui.click(x=674, y=687, duration=0.5)
    pyautogui.click(x=674, y=687, duration=0.5)
    pyautogui.click(x=674, y=687, duration=0.5)

    pyautogui.click(x=642, y=720, duration=0.5)
    pyautogui.click(x=642, y=720, duration=0.5)
    pyautogui.click(x=642, y=720, duration=0.5)
    pyautogui.click(x=642, y=720, duration=0.5)

    pyautogui.click(x=584, y=622, duration=0.5)
    pyautogui.click(x=594, y=548, duration=0.5)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')


def enviarMensagem():
    rotation = True
    sistemaAntiBug = 0
    runs = 0

    personNamePosition = []
    PersonMessagePosition = []

    for i in range(20):
        personNamePosition.append(
            "//*[@id='pane-side']/div[1]/div/div/div[{0}]/div/div/div[2]/div[1]/div[1]/span/span".format(i))
        PersonMessagePosition.append(
            "//*[@id='pane-side']/div[1]/div/div/div[{0}]/div/div/div[2]/div[2]/div[1]/span/span".format(i))

    driver = webdriver.Chrome(port=61879)
    driver.get('http://web.whatsapp.com')

    msg = "TV reiniciada com sucesso!"
    input('Enter anything after scanning QR code')

    while sistemaAntiBug < 3:
        for i in range(len(personNamePosition)):
            try:
                user = driver.find_element_by_xpath(
                    personNamePosition[i])
                texto = driver.find_element_by_xpath(
                    PersonMessagePosition[i])
                if "REINICIAR TV - CENTRAL DE ATENDIMENTO" in texto.text:
                    print("A pessoa e: "+user.text+"\t"+texto.text)
                    print("/n/n Executar REINICIO!")
                    reiniciarTV()
                    userText = driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(user.text))
                    userText.click()
                    msg_box = driver.find_element_by_xpath(
                        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                    msg_box.send_keys(msg)
                    button = driver.find_element_by_xpath(
                        "//*[@id='main']/footer/div[1]/div[3]/button/span")
                    button.click()
                    sistemaAntiBug += 1
                if "DERRUBAR LAB 1" in texto.text and user.text == "Odair Unisal":
                    print("Derrubando Laboratoirio 1")
                if "DERRUBAR LAB 2" in texto.text and user.text == "Odair Unisal":
                    print("Derrubando Laboratoirio 2")

                runs += 1
                if runs % 10 == 0:
                    data = str(datetime.now())
                    with open("{0}.txt".format(datetime.now().date), "a", encoding="utf-8") as f:
                        f.write(data+"\t"+user.text+"\t"+texto.text+"\n")
                        f.close()
                    sistemaAntiBug = 0
                    print("AntiBug:"+str(sistemaAntiBug))
            except:
                pass
            finally:
                time.sleep(10)
                if rotation:
                    pyautogui.move(None, 3)
                    rotation = False
                else:
                    pyautogui.move(None, -3)
                    rotation = True


enviarMensagem()
# desligarLab1()

"""
CARTA SENHA AUTOMATICA

 if "CARTA SENHA 123456:" in texto.text:
                    print("Enviando Carta Senha")
                    driver.find_element_by_tag_name(
                        'body')
                    driver.execute_script(
                        '''window.open("http://senha.liceu.com.br","_self");''')
                    time.sleep(10)
                    campoRA = driver.find_element_by_id("ra")
                    campoRA.click()
                    pyautogui.typewrite("170001118", interval=.1)
                    time.sleep(2)
                    nomeRA = driver.find_element_by_xpath(
                        "//*[@id='dadosAluno']/span[1]")
                    botao = driver.find_element_by_xpath(
                        "//*[@id='fichaInscricao']/fieldset/div[1]/div[2]/button")
                    botao.click()
                    pastaArquivo = "C:\\Users\\luiz.camargos\\Downloads\\{0}.pdf".format(
                        nomeRA.text)
                    driver.execute_script(
                        '''window.open("http://web.whatsapp.com","_self");''')
                    time.sleep(10)
                    userText = driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(user.text))
                    userText.click()
                    print("clicado no Nome")
                    botao = driver.find_element_by_xpath(
                        "//*[@id='main']/header/div[3]/div/div[2]/div/span")
                    botao.click()
                    botao = driver.find_element_by_xpath(
                        "//*[@id='main']/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button")
                    botao.click()
                    time.sleep(.5)
                    pyautogui.typewrite(pastaArquivo)
                    pyautogui.press("enter")
"""
