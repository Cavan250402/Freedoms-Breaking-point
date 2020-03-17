from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()
#Hide the turtle
turtle.hideturtle()
screen.tracer(False)


def Square(x,y,size,colour):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown
    #Selecting colours of sides and and Square
    turtle.pencolor("black")
    turtle.fillcolor(colour)
    #Beggining the fill
    turtle.begin_fill()

    for i in range (4):
        turtle.forward(size)
        turtle.right(90)

    turtle.end_fill()

    
#Update turtle to make it go instantly



screen.update()
