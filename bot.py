# https://www.youtube.com/watch?v=bf_UOFFaHiY
# http://www.trex-game.skipser.com/
from PIL import ImageGrab, ImageOps
import pyautogui
import time
from numpy import *

class Cordinates():
    replayBtn = (962, 530)
    dinosaur = (664, 536) # dinaosaur standing
    # dinosaur = (686, 548) # dinosaur down
    #730= x cordinate to check for tree
    #y cordinate = 565

def restartGame():
    pyautogui.click(Cordinates.replayBtn)
    # pyautogui.keyDown('down')

def pressSpace():
    # pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    print("Jump")
    time.sleep(0.18)
    pyautogui.keyUp('space')
    # pyautogui.keyDown('down')

def imageGrab():
    x1 = Cordinates.dinosaur[0] + 50 # 70 is the distance
    y1 = Cordinates.dinosaur[1] 
    x2 = x1 + 80
    y2 = Cordinates.dinosaur[1] + 35
    box = (x1, y1, x2, y2)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

def main():
    restartGame()
    try:
        while True:
            # imageGrab()
            if(imageGrab() != 3047):
                pressSpace()
                time.sleep(0.1)
    except KeyboardInterrupt:
        print("Program stopped")

main()