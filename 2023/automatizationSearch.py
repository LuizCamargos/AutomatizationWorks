import pyautogui
import time
import random
import os
import requests
import json


def startUp(lines):
    # timer to start
    time.sleep(3)
    # write line
    random.shuffle(lines)
    return lines


def readLines():
    # Open Local File
    cwd = os.getcwd()
    f = open(cwd+'/2023/solutions.txt', 'r')
    # read Lines from file
    lines = f.readlines()
    return lines


def keyboardPress(line):
    pyautogui.write(line, interval=.125)
    pyautogui.press(['enter'])
    time.sleep(2)
    pyautogui.hotkey(['down', 'down', 'down'], interval=.3)
    time.sleep(2)


def keyboardHotKey(keys):
    pyautogui.hotkey(keys, interval=.1)


def moveMousePosition(x, y):
    pyautogui.moveTo(x=x, y=y, duration=3, tween=(pyautogui.easeInOutQuad))


def autoCompleteSearch(text):
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"}
    response = requests.get(
        'http://google.com/complete/search?client=chrome&q='+text, headers=headers)
    question = json.loads(response.text)[1]
    question = question[random.randint(0, len(json.loads(response.text)[1]))]
    return question


lines = readLines()
lines = startUp(lines)
count = qtd = 0
for line in lines:
    qtd += 1
    try:
        line = line.rstrip()
        question = autoCompleteSearch(line)
        print("{}. {}".format(count, question))
        keyboardHotKey(['ctrl', 'e'])
        keyboardPress(question)
        count += 1
        if count == 35:
            keyboardHotKey(['f12'])
        if count == 70:
            print("Finish: {}/{}".format(count, qtd))
            break
    except:
        pass


###############################################################################
# Get time
# time = datetime.now().time()
