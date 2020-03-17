import turtle as t
#Hide the turtle
t.hideturtle()
t.tracer(False)

def Square(x,y,size,colour):
    #Moving the Pen 
    t.penup()
    t.goto(x,y)
    t.pendown()
    #Selecting colours of sides and and Square
    t.pencolor("black")
    t.fillcolor(colour)
    #Beggining the fill
    t.begin_fill()

    for i in range (4):
        t.forward(size)
        t.right(90)

    t.end_fill()



#Update turtle to make it go instantly
t.update()
