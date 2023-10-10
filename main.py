import pyautogui as pag
from PIL import Image
import time
"""region = 900 500 100 100, RGB 68,252,234    Arrow: 1750,875,150,150
pag.FAILSAFE=True
Bub1=Image.open(f"assets/Bubble.png")
Bub2=Image.open(f"assets/Bubble2.png")
Bubbles=[Bub1,Bub2]"""
count=0
moveup,moveside='w','a'
flag=True
while flag:
    pag.click()
    while count<140:
  
        for x in range(100):
               if pag.pixelMatchesColor(x+900,530,(68,252,234),tolerance=5):
                    count+=1
                    print("Seen "+str(count))
                    for y in range(7):
                      pag.leftClick()
                      time.sleep(3.0/7)
                    pag.leftClick()
                    time.sleep(.5)
                    break
        print("Not Seen "+ str(count))
        time.sleep(1)
    
    pag.press('esc')
    pag.press('r')    
    pag.press('enter')
    time.sleep(6)
    pag.keyDown('o')
    time.sleep(.6)
    pag.keyUp('o')
    if pag.pixelMatchesColor(365,554,(159,214,47),tolerance=30):
        moveup,moveside='s','d'
    else:
        moveup,moveside='w','a'
    pag.keyDown(moveup)
    time.sleep(6)
    pag.keyUp(moveup)
    time.sleep(1)
    pag.keyDown('space')
    time.sleep(.3)
    pag.keyUp('space')
    pag.keyDown(moveside)
    time.sleep(1)
    pag.keyUp(moveside)
    pag.keyDown(moveup)
    time.sleep( 6.5)
    pag.keyUp(moveup)
    pag.press('e')
    time.sleep(2)
    pag.press('|')
    time.sleep(.5)
    pag.keyDown('s')
    time.sleep(.2)
    pag.keyUp('s')
    pag.press("enter")
    time.sleep(.5)
    pag.press('|')
    time.sleep(1)
    pag.keyDown('s')
    time.sleep(.2)
    pag.keyUp('s')
    pag.press("enter")
    pag.press('enter')
    time.sleep(.5)
    pag.press('esc')
    pag.press('r')    
    pag.press('enter')
    time.sleep(6)
    if pag.pixelMatchesColor(365,554,(159,214,47),tolerance=15):
        pag.keydown('right')
        time.sleep(2.5)
        pag.keyUp('right')
    moveup,moveside='w','a'
    pag.keyDown(moveup)
    time.sleep(8)
    pag.keyUp(moveup)
    pag.keyDown('i')
    time.sleep(1)
    pag.keyUp('i')

