from inspect import trace
from turtle import *
from random import random
from base import line

def draw():
    #darwing a maze 
    color('black')
    width(5)
    for x in range(-200,200,40):
        for y in range(-200,200,40):
            #create matrix 
            if random()>0.5:
                line(x,y,x+40,y+40)
            else:
                line(x,y+40,x+40,y)

    update()

def tap(x,y):
    #draw line/dot for the user on the screen when he clicks
    if abs(x) > 198 or abs(y) > 198:
        up()
    else:
        down()
    width(2)
    color('red')
    goto(x,y)
    dot(4)

setup(420,420)
hideturtle()
trace(False)

draw()
onscreenclick(tap)
done()