from turtle import Screen, Turtle

RedInfantry = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\InfantryRedV20.gif"

def InfantryRed(x, y):
    turtle = Turtle()
    turtle.shape(RedInfantry)
    turtle.penup()
    turtle.goto(x, y)

    return turtle

screen = Screen()
screen.addshape(RedInfantry)

infantry_1 = InfantryRed(200, -200)
infantry_2 = InfantryRed(-200, 200)
#infantry_3 = InfantryRed(-200, -200)

infantry_1.goto(200, 200)

screen.exitonclick()
