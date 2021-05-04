# import the random and turtle libraries
from random import *
from turtle import *
  
#Setting the screen
screen = Screen()
  
#choose background color, i chose red
screen.bgcolor("red")
  
# define the function, creates a square for the game
def Square(x, y):
    up()
    goto(x, y)
    down()
    color('white', 'yellow')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()
  
#Define function..keeps check of the index number

def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
  
#Define the function
def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200
  
# Make the function interactive through user clicks
def click(x, y):
    spot = Numbering(x, y)
    mark = state['mark']
  
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
  
def draw():
    clear()
    goto(0, 0)
    stamp()
  
    for count in range(64):
        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)
  
    mark = state['mark']
  
    if mark is not None and hide[mark]:
        
        x, y = Coordinates(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))
  
    update()
    ontimer(draw, 10)
  
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
  
# Shuffles the numbers inside of the tiles, so every time you play it's different

shuffle(tiles)
tracer(False)
onscreenclick(click)
draw()
done()