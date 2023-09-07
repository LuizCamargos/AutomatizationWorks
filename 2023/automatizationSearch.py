import pyautogui
import time
import random
import os


def startUp(lines):
    # timer to start
    time.sleep(3)
    # write line
    random.shuffle(lines)
    return lines


def readLines():
    # Open Local File
    cwd = os.getcwd()
    f = open(cwd+'/2023/data.txt', 'r')
    # read Lines from file
    lines = f.readlines()
    return lines


def keyboardPress(line, i):
    pyautogui.write(line, interval=.125)
    pyautogui.press(['tab']*2, interval=2)
    time.sleep(1)
    pyautogui.press(['enter'])
    time.sleep(2)
    pyautogui.hotkey(['down', 'down', 'down'], interval=.3)
    time.sleep(2)
    print(i)


def keyboardHotKey(keys):
    pyautogui.hotkey(keys, interval=.1)


def moveMousePosition(x, y):
    pyautogui.moveTo(x=x, y=y, duration=3, tween=(pyautogui.easeInOutQuad))


lines = readLines()
lines = startUp(lines)

for line in lines:
    keyboardPress(line, lines.index(line))
    keyboardHotKey(['ctrl', 'e'])
    moveMousePosition(random.randint(300, 1000), random.randint(300, 1000))


###############################################################################

# Get time
# time = datetime.now().time()
