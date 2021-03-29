import pyautogui as bot
import time
revision = "1C"
rango = 84
fechaLiberacion = "08/03/2021"
# Number of page
# X: 1159 Y:  273

#Empty space
# X: 1292 Y:  317 RGB: (230, 230, 230)

#REVISION
#X: 1014 Y:  278 RGB: (255, 255, 255)

#Fecha de liberacion
#X:  689 Y:  278 RGB: (255, 255, 255)
time.sleep(5)
for i in range(1,rango+1):
    bot.click(1159, 273, 3)
    time.sleep(0.2)
    pages = (str(i)+" de "+str(rango))
    bot.write(pages)
    bot.click(1014,278,3)
    bot.sleep(0.2)
    bot.write(revision)
    bot.click(689,278,3)
    bot.sleep(0.2)
    bot.write(fechaLiberacion)
    bot.click(1292,317)
    bot.sleep(0.2)
    bot.press("down")
    time.sleep(0.2)
