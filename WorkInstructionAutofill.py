import pyautogui as pag
import time
import pyperclip
import GUI
import tkinter

def getValues():
    global rev
    rev = GUI.getRev()
    global pageRange
    pageRange = GUI.getPages()
    global endDate
    endDate = GUI.getEndDate()
    global title
    title = GUI.getTitle()
    global documentCode
    documentCode = GUI.getDocumentNumber()

def getSwitchStates():
    # SWITCHES
    global revSwitch
    if rev != "": revSwitch = True
    else: revSwitch = False

    global dateSwitch
    if endDate != "": dateSwitch = True
    else: dateSwitch = False

    global titleSwitch
    if title != "": titleSwitch = True
    else: titleSwitch = False

    global pagesSwitch
    if pageRange != "": pagesSwitch = True
    else: pagesSwitch = False

    global codeSwitch
    if documentCode != "": codeSwitch = True
    else: codeSwitch = False

#COORDS
titleCords = [796,256]
pagesCords = [1125,290]
revCords = [998, 291]
dateCords = [721,284]
codeCords = [1082,253]
emptySpaceCords = [1252, 400]


def setPP():
    # pag.hotkey('alt', 'space')
    # pag.press('n')
    if pag.getActiveWindowTitle()[-10:] != "PowerPoint":
        pag.alert("Abra la instruccion a modificar, y después presione Iniciar")
        exit()
    else:
        pag.alert("Comenzará la modificación automática")
        pag.press('alt')
        pag.press('w')
        pag.press('f')
        pag.press('2')


def getInstructionTitle():
    global title
    pyperclip.copy(title)





def general():
    print("Page range: "+str(pageRange))
    for i in range(1, pageRange + 1):
        if titleSwitch:
            for j in range(3):
                pag.click(titleCords[0], titleCords[1], 3)
                pag.press('delete')
            pag.sleep(0.1)
            pag.hotkey('ctrl', 'v')
        else:
            pag.click(titleCords[0], titleCords[1])

        pag.press('tab',2)
        if codeSwitch:
            pag.sleep(0.1)
            pag.write(documentCode)

        pag.press('tab',2)
        if dateSwitch:
            pag.sleep(0.1)
            pag.write(endDate)

        pag.press('tab', 2)
        if revSwitch:
            pag.sleep(0.1)
            pag.write(rev)
        pag.press('tab', 2)
        if pagesSwitch:
            time.sleep(0.1)
            pages = (str(i) +" de " + str(pageRange))
            print(pages)
            print(i)
            pag.write(pages)




        pag.click(emptySpaceCords)
        pag.sleep(0.1)
        pag.press("down")
        time.sleep(0.2)
    pag.alert("Actualización de información completada.")


GUI.startGui()
time.sleep(0.2)
pag.click(emptySpaceCords)
setPP()
getValues()
getInstructionTitle()
getSwitchStates()
time.sleep(0.2)
general()
print(GUI.getPages(), GUI.getTitle())