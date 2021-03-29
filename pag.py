import pyautogui as pag
import time

def showDesktop():
    pag.hotkey('win','d')


def findAndClickSimple(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         break

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndClick(img, timeLimit, conf, doubleClick):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         pag.alert("Ocurrio un error, solicite apoyo al técnico de pruebas")
         exit()

    if doubleClick:
         pag.doubleClick(cords)
    else:
         pag.click(cords)

def findAndBool(img, timeLimit, conf):
    cords = None
    timeLimit = (timeLimit/0.4)
    i = timeLimit
    while cords is None:
     if i > 0:
        i=i-1
        cords = pag.locateCenterOnScreen(img, confidence=conf)
        time.sleep(0.2)
     else:
         print('Out')
         pag.alert("An error ocurred")
         exit()

     return True
