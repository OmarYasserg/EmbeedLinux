import pyautogui
import time
def ReadUnreadMails():
    pyautogui.press('win')  
    time.sleep(.5)
    pyautogui.write('outlook')
    pyautogui.press('enter') 
    time.sleep(1.5)
    pyautogui.click(830,554, duration=1.2)
    pyautogui.click(705,455, duration=1.2)
    pyautogui.click(529,166, duration=1.2)
    pyautogui.click(529,252, duration=1.2)
    pyautogui.click(438,285, duration=1)
    for i in range(50):
        pyautogui.press('down') 
        time.sleep(.6)
    
    # pyautogui.mouseInfo()

ReadUnreadMails()