import pyautogui
import time
import pydirectinput
import keyboard
pyautogui.FAILSAFE = False
while 1:
    afk = pyautogui.locateCenterOnScreen(r'G:\fishing\afk.png',confidence=0.8,grayscale = True)
    afk1 = str(afk)
    
    if("Point" in afk1):
        pyautogui.press("w")
        pyautogui.press("w")
        pyautogui.press("s")
        pyautogui.press("s")
    while 1:
        pyautogui.moveTo(957,536)
        pydirectinput.moveTo(1496,218)
        cikis = pyautogui.locateCenterOnScreen(r'G:\fishing\fishing.png',confidence=0.7,grayscale = True)
        cikis1 = str(cikis)
        if("Point" in cikis1):
            pyautogui.mouseDown(button='left')
            time.sleep(1.89)
            pyautogui.mouseUp(button='left')
            break
    while 1:
        a = pyautogui.locateCenterOnScreen(r'G:\fishing\hook.png',confidence=0.8,grayscale = True)
        a1 = str(a)
        b = pyautogui.locateCenterOnScreen(r'G:\fishing\olta.png',confidence=0.8,grayscale = True)
        b1 = str(b)
        if("Point" in a1 or "Point" in b1):
            pyautogui.click(button="left")
            break
        
    
    while 1:
        x = pyautogui.locateCenterOnScreen(r'G:\fishing\durum1.png',confidence=0.8,grayscale = True)
        x1 = str(x)
        y = pyautogui.locateCenterOnScreen(r'G:\fishing\durum2.png',confidence=0.8,grayscale = True)
        y1 = str(y)
        z = pyautogui.locateCenterOnScreen(r'G:\fishing\durum3.png',confidence=0.7,grayscale = True)
        z1 = str(z)
        t = pyautogui.locateCenterOnScreen(r'G:\fishing\fishing.png',confidence=0.7,grayscale = True)
        t1 = str(t)
        brim = pyautogui.locateCenterOnScreen(r'G:\fishing\brim.png',confidence=0.7,grayscale = True)
        brim1 = str(brim)
        if("Point" in brim1):
            pyautogui.doubleClick(button="left")
            break
        if(keyboard.is_pressed =="q"):
            break
        if("Point" in z1 or "Point" in y1 or "Point" in x1):
            pyautogui.mouseUp(button='left')
        else:
            pyautogui.mouseDown(button='left')
        