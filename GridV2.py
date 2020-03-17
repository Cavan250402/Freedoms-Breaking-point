import turtle as t
from SquareV2 import *


Square(25,"Green")
x = -300
y = 300

for i in range(25):
    x = x + (i*25)

    t.penup()
    t.goto(x,y)
    t.pendown()

    Square(25,"Green")
