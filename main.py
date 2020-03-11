from selenium import webdriver
import pyautogui
import time
driver = webdriver.Chrome()
driver.get('http://web.whatsapp.com')


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

    name = "Naty Unisal"
    msg = "Televisor Reiniciado com sucesso! \n Caso Contrario envie outra mensagem que o Luiz irá ler :D"

    # Scan the code before proceeding further
    input('Enter anything after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_elements_by_class_name('copyable-text')
    print(msg_box[-1])

    #msg_box = driver.find_element_by_class_name('input-container')
    # msg_box.send_keys(msg)
    #button = driver.find_element_by_class_name('input-container')
    # button.click()
    # resposta msg_box = [<selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="8dcab944-a2be-478e-a6e2-3e7ea937c840")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="726ac3b0-c1f2-49c6-8ab1-be8432871ca1")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="b6c1deb4-7a08-4a2d-bfd5-2d46ff409954")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="dffd226d-34fe-4a04-9a2c-2b81ce6c35b2")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="5ecda373-750a-441d-9309-da12dd61101c")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="77e2b384-b74b-4184-b3b2-2f5af80766cc")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="0f00d462-d9ae-4960-b3d3-8597ea2783f1")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="53ea6340-28af-469a-8422-ce49b9343908")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="2c0f3877-eb0a-4dae-86be-1bc7f1601abf")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="cbf35c26-2099-4c45-8ea6-1e6263a66da9")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="0ae829f7-7446-4762-8d32-781e7372bd42")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="bc01927a-b89c-4a1d-87eb-b6ac276657f5")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="d7f17689-dcc9-47b0-a014-1c29922424a9")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="7f1abd70-cf81-4717-8ed6-950ed8e2c032")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="f4a5aa04-5768-4b4f-afe8-d21cc276d5e0")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="d437ff52-a641-4c1e-8bff-6a416a4bfeac")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="2afb8010-cc08-461a-9382-b4b655a082ed")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="77c04b6e-20c9-4592-a324-b882b810a451")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="513658bf-4447-4522-b5f6-e539889fa361")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="26728a67-aad4-4477-af89-9889677141da")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="872fdbb1-7dfb-4bf5-91c4-91965bda0bbb")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="bc606653-5272-4a35-94f3-8313d32024d9")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="db0a36c1-1bca-4413-9bb6-a91d1330a4f2")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="81837c59-148a-4315-af12-3aad24c17c1e")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="fd4a7953-9bc0-4e0d-ac2d-1e6539c15d67")>, <selenium.webdriver.remote.webelement.WebElement (session="23d9c061eb4dbe8baccde5f4754437b6", element="81abe8b3-8374-4924-9a25-dc78e30c5564")>]


enviarMensagem()
