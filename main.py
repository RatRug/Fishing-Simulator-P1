import pyautogui as pag
from PIL import Image
import time
"""region = 900 500 100 100, RGB 68,252,234
coords=pag.locateOnScreen(Bubbles[1],confidence=.75)
if coords is not None:
    pag.moveTo(coords)
print(coords)
pag.displayMousePosition()"""
pag.FAILSAFE=True
Bub1=Image.open(f"assets/Bubble.png")
Bub2=Image.open(f"assets/Bubble2.png")
Bubbles=[Bub1,Bub2]
count=0
pag.click()
print("FF")
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
    
