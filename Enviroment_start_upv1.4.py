import turtle as t
t.tracer(False)
t.hideturtle()



def creationMovePlace(x,y):

    t.up()
    t.goto(x,y)
    t.down()


def createSquare(x,y,side):
    creationMovePlace(x,y)
    t.fillcolor("green")
    t.begin_fill()
    for i in range(4):
        t.forward(side)
        t.right(90)
    x = x+side
    creationMovePlace(x,y)
    t.end_fill()

def grid():
    for i in range(25):
        createSquare(-350+i*25,350,25)
        for j in range(25):
            createSquare(-350+i*25,325-j*25,25)






grid()




