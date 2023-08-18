import pyautogui
import time

def installExtensionVSCode(extensionName):
    pyautogui.press('win')  
    time.sleep(0.8)
    pyautogui.write('vscode')
    pyautogui.press('enter')  
    pyautogui.click(1625,23,duration=1)
    pyautogui.click(40,450,duration=1)
    pyautogui.click(415,155,duration=1)
    for i in range(12):  
        pyautogui.press('backspace')
    time.sleep(0.8)
    pyautogui.write(extensionName)
    pyautogui.click(671,298,duration=2.5)
    time.sleep(1.5)

installExtensionVSCode("c++ helper")
installExtensionVSCode("cmake tools")
