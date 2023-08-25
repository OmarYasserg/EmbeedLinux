import pyautogui
import datetime
import time
# Keyboard



def installExtensionVSCode(extensionName):
    pyautogui.press('win')  
    time.sleep(0.8)
    pyautogui.write('vscode')
    pyautogui.press('enter') 
    time.sleep(1.5)
    pyautogui.click(1400,235,duration=2)
    time.sleep(1.5)
    pyautogui.click(27,299,duration=2)
    # pyautogui.mouseInfo()
    pyautogui.click(368,107,duration=1)
    for i in range(12):  
        pyautogui.press('backspace')
    time.sleep(0.8)
    pyautogui.write(extensionName)
    pyautogui.mouseInfo()
    # pyautogui.click(529,297,duration=2.5)
    # time.sleep(1.5)
    

installExtensionVSCode("c++ helper")

# installExtensionVSCode("c++ helper")
