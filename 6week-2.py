import random
from tkinter.simpledialog import *
import turtle


def getsring() :
    retstr = ""
    retstr = askstring("문자열 입력", "거북이가 쓸 문자열 입력")
    return retstr

def getRGB() :
    r , g, b = 0,0,0
    r = random.random()
    g = random.random()
    b = random.random()
    return(r,g,b)

def getXYAS(sw,sh) :
    x,y, angle, size = 0 , 0 , 0 , 0
    x=random.randrange(int(-sw/2) , int(sw/2))
    y = random.randrange(int(-sh/2) , int(sh/2))
    angle = random.randrange(0,360)
    size = random.randrange(10,50)
    return [x,y,angle,size]

inStr = ""
swidth, sheight = 300 , 300
tX , tY , tAngle, tSize = [0] * 4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width = swidth + 50 , height = sheight +50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

inStr = getsring()

for ch in inStr:
    tX, tY, tAngle , txtSize = getXYAS(swidth,sheight)
    r , g , b = getRGB()

    turtle.goto(tX,tY)
    turtle.left(tAngle)

    turtle.pencolor((r,g,b))
    turtle.write(ch, font = ("맑은고딕", txtSize, "bold"))

turtle.done()