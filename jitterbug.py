import pyautogui
import time

while True:
    pyautogui.moveRel(0, 10)
    pyautogui.moveRel(0, -10)
    time.sleep(5)