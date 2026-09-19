import pyautogui as py
import time


time.sleep(3)
py.press("esc")

scroll = 150

def first_move(range1):
    global scroll
    for i in range(range1):
        time.sleep(0.01)
        py.leftClick()
        time.sleep(0.01)
        py.rightClick()
        time.sleep(0.01)

        py.scroll(scroll)
        scroll *= -1

        time.sleep(0.01)
        py.rightClick()
        time.sleep(0.01)
        py.rightClick()
        time.sleep(0.01)
        py.rightClick()
        time.sleep(0.01)

        py.scroll(scroll)
        scroll *= -1

        py.keyDown("w")
        time.sleep(0.14) 
        py.keyUp("w")

def look_lift():

    py.keyDown("a")
    time.sleep(0.16) 
    py.keyUp("a")

    py.moveRel(-115,0,1) 

    py.keyDown("w")
    time.sleep(0.15)
    py.keyUp("w")

def look_right():

    py.keyDown("d")
    time.sleep(0.16) 
    py.keyUp("d")

    py.moveRel(115,0,1) 

    py.keyDown("w")
    time.sleep(0.15)
    py.keyUp("w")

first_move(4)
look_lift()
first_move(4)
look_right()
first_move(3)
look_lift()
first_move(3)
#look_right()
#first_move(3)
#look_lift()
#first_move(3)
