import tkinter as tk
import tkcalendar
import datetime
import pyautogui as pag
import re

title = ""
endDate = ""
rev = ""
pages = 0
documentNumber = ""

#DEFINING REGEX
def documentNumberRegex(text):

    x = re.search("[a-zA-z]{2},[.],[0-9]{3}", text)
    return x;

def getTitle():
    global title
    return title


def getPages():
    global pages
    return pages


def getRev():
    global rev
    return rev


def getEndDate():
    global endDate
    return endDate


def getDocumentNumber():
    global documentNumber
    return documentNumber

def destroyWindow():
    global root
    root.destroy()

def startGui():
    date = datetime.datetime.now()
    year = date.strftime("%Y")
    month = date.strftime("%m")
    today = date.strftime("%d")

    fontStyle = eval("'ARIAL', 14, 'bold'")
    rightMargin = eval("(0,50)")




    def startProcess():
        dateLabel.config(text=calendar.get_date())
        global title
        title = titleEntry.get()

        global endDate
        endDate = selectedDateLabel.cget("text")

        global rev
        rev = revEntry.get()

        global pages
        try:
            pages = eval(pagesEntry.get())
        except:
            pag.alert("Por favor Introduzca el número de páginas")
            return

        global documentNumber
        documentNumber = "MMC-WI-"+documentNumberEntry.get()

        root.destroy()

    def updateDate():
        selectedDateLabel.config(text=calendar.get_date())


    root = tk.Tk()
    root.title("Documentation bot")

    mainTitleLabel = tk.Label(root, text="Modificar Instrucción de trabajo")
    mainTitleLabel.config(font=('Arial', 18, 'bold'))

    documentNumberLabel = tk.Label(root, text="No. documento: MMC-WI-")
    documentNumberLabel.config(font=(fontStyle))
    documentNumberEntry = tk.Entry(root, width=10)

    titleLabel = tk.Label(root, text="Titulo:")
    titleLabel.config(font=(fontStyle))
    titleEntry = tk.Entry(root, width=45)
    titleEntry.config(font=fontStyle)

    endDateLabel = tk.Label(root, text="Fecha de Liberación:")
    endDateLabel.config(font=(fontStyle))
    selectedDateLabel = tk.Label(root)
    selectedDateLabel.config(font=fontStyle)

    updateDateButton = tk.Button(text="Seleccionar Fecha", command=updateDate)
    updateDateButton.config(font=fontStyle)

    revLabel = tk.Label(root, text="Revisión:")
    revLabel.config(font=(fontStyle))
    revEntry = tk.Entry(root, width=9)

    pagesLabel = tk.Label(root, text="   No. de Hojas:")
    pagesLabel.config(font=(fontStyle))
    pagesEntry = tk.Entry(root, width=10)

    dateLabel = tk.Label(text="")
    dateLabel.config(font=('ARIAL',14,'bold'), borderwidth=2, relief="solid", highlightbackground="green")
    calendar = tkcalendar.Calendar(selectmode='day', month=int(month), year=int(year), day=int(today), locale='es_mx')
    startButton = tk.Button(text="Iniciar", command=startProcess)
    startButton.config(font=('ARIAL', 15, 'bold'), fg='green')

    mainTitleLabel.grid(column=0, row=1, columnspan=6, pady=(10, 20))
    titleLabel.grid(column=0, row=2, sticky="E", padx=(30,0))
    titleEntry.grid(column=1, row=2, sticky="w")
    documentNumberLabel.grid(column=4, row=2, columnspan=1, sticky="E", padx=(30,0))
    documentNumberEntry.grid(column=3, row=2, columnspan=3, sticky="E", padx=rightMargin)
    endDateLabel.grid(column=0, row=3, padx=(30,0), columnspan=2)
    selectedDateLabel.grid(column=1, row=3, sticky="E", padx=(0,60))
    revLabel.grid(column=3, row=3, sticky="w", padx=(30,0))
    revEntry.grid(column=4, row=3, sticky="w")
    pagesLabel.grid(column=4, row=3, sticky="E")
    pagesEntry.grid(column=5, row=3, sticky="W", padx=rightMargin)
    calendar.grid(column=0, row=4, sticky="wE", columnspan=3, padx=(100,0), pady=(20,0))
    updateDateButton.grid(column=1,row=5, columnspan=2, sticky="nesw", pady=(5,30))
    startButton.grid(column=3, row=4, sticky="WES", padx=(20,50), columnspan=3)

    updateDate()

    root.mainloop()


