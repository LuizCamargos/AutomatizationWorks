from selenium import webdriver
import pyautogui
import time
from datetime import datetime
from twilio.rest import Client
sistemaAntiBug = 0

datetime.now()


def reiniciarTV():
    pyautogui.FAILSAFE = False

    senha = "master"
    ip = "10.40.102.23"

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


def enviarMensagem():
    sistemaAntiBug = 0
    runs = 0

    personNamePosition = ["//*[@id='pane-side']/div[1]/div/div/div[17]/div/div/div[2]/div[1]/div[1]/span/span",
                          "//*[@id='pane-side']/div[1]/div/div/div[16]/div/div/div[2]/div[1]/div[1]/span/span",
                          "//*[@id='pane-side']/div[1]/div/div/div[15]/div/div/div[2]/div[1]/div[1]/span/span",
                          "//*[@id='pane-side']/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span/span",
                          "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]/span/span"]
    PersonMessagePosition = ["//*[@id='pane-side']/div[1]/div/div/div[17]/div/div/div[2]/div[2]/div[1]/span/span",
                             "//*[@id='pane-side']/div[1]/div/div/div[16]/div/div/div[2]/div[2]/div[1]/span/span",
                             "//*[@id='pane-side']/div[1]/div/div/div[15]/div/div/div[2]/div[2]/div[1]/span/span",
                             "//*[@id='pane-side']/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div[1]/span/span",
                             "//*[@id='pane-side']/div[1]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/span/span"]

    driver = webdriver.Chrome()
    driver.get('http://web.whatsapp.com')

    msg = "Bomba Lancada com Sucesso! \n Caso voce continue vivo porfavor faca novamente ;D"
    input('Enter anything after scanning QR code')

    while sistemaAntiBug < 3:
        for i in range(5):
            try:
                user = driver.find_element_by_xpath(
                    personNamePosition[i])
                texto = driver.find_element_by_xpath(
                    PersonMessagePosition[i])
                if "AUTODESTRUICAO" in texto.text:
                    print("A pessoa e: "+user.text+"\t"+texto.text)
                    print("/n/n Executar AUTODESTRUICAO!")
                    # reiniciarTV()
                    user = driver.find_element_by_xpath(
                        '//span[@title = "{}"]'.format(user.text))
                    user.click()
                    msg_box = driver.find_element_by_xpath(
                        "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
                    msg_box.send_keys(msg)
                    button = driver.find_element_by_xpath(
                        "//*[@id='main']/footer/div[1]/div[3]/button/span")
                    button.click()
                    sistemaAntiBug += 1
                elif "QUERO DERRUBAR O LAB 1" in texto.text and user.text == "Odair Unisal":
                    print("Derrubando Laboratoirio 1")
                elif "QUERO DERRUBAR O LAB 2" in texto.text and user.text == "Odair Unisal":
                    print("Derrubando Laboratoirio 2")
                data = str(datetime.now())
                with open("relatorio.txt", "a", encoding="utf-8") as f:
                    for i in range(3):
                        f.write(data+"\t"+user.text+"\t"+texto.text+"\n")
                    f.close()
                runs += 1
                if runs % 5 == 0:
                    sistemaAntiBug = 0
                print("AntiBug:"+str(sistemaAntiBug))
            except:
                pass
            finally:
                time.sleep(20)


enviarMensagem()
