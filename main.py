from selenium import webdriver
import pyautogui
import time


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
    driver = webdriver.Chrome()
    driver.get('http://web.whatsapp.com')

    name = "PAIZAO"
    msg = "TV Reiniciada com sucesso! \n Caso Contrario envie outra mensagem com outro Texto que o Luiz irá ler :D"
    input('Enter anything after scanning QR code')

    while True:
        src = driver.page_source
        if ("AUTODESTRUICAO NA TV!" in src):
            print("/n/n Executar AUTODESTRUICAO!")
            user = driver.find_element_by_xpath(
                '//span[@title = "{}"]'.format(name))
            user.click()
            msg_box = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            msg_box.send_keys(msg)
            button = driver.find_element_by_xpath(
                "//*[@id='main']/footer/div[1]/div[3]/button/span")
            button.click()
       else:
            with open("relatorio.html", "w", encoding="utf-8") as f:
                f.write(src)
                f.close()
        time.sleep(180)


enviarMensagem()
