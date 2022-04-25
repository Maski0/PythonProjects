from turtle import *
from base import line

#unDone

def grid():
    # Tic Tac toe map (Grid)
    line(-67,200,-67,-200) #vertical lines
    line(67,200,67,-200)
    line(-200,-67,200,-67) #Horizontal lines
    line(-200,67,200,67)

def drawx(x,y):
    # Draws X player
    line(x,y,x+133,y+133)
    line(x,y+133,x+133,y)

def drawo(x,y):
    # Draws O Player
    up()
    goto(x+67,y+5)
    down()
    circle(62)

def floor(value):
    return ((value+200)//133) * 133 - 200 #offset is 200, size is 133

state = {'player' : 0}
players = [drawx,drawo]
moves = {
    '1,1' : 0, '1,2' : 0, '1,3' : 0,
    '2,1' : 0, '2,2' : 0, '2,3' : 0,
    '3,1' : 0, '3,2' : 0, '3,3' : 0,
    
}
drig = []
def canplace(move):
    return 

def tap(x,y):
    #draw X or O on tapped surface
    if canplace():
        x = floor(x)
        y = floor(y)
        player = state['player']
        draw = players[player]
        draw(x, y)

        update()
        state['player'] = not player
    

setup(420,420)
hideturtle()
tracer(False)
grid()
update()

onscreenclick(tap)

done()