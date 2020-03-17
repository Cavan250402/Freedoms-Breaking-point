import turtle as t

t.tracer(False)
t.hideturtle()

t.color("#000000")
t.pencolor("black")

#A function to draw a box
def PixelBox(size):
    t.begin_fill()
    for s in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.setheading(0)

boxSize = 25
#Positoning turtle to the top left of the screen

t.penup()
t.forward(-300)
t.setheading(90)
t.forward(325)
t.setheading(0)
def Infantry_Red():
    #       White       Red     Cream       Grey    Black       Pink
    colours=["#ffffff","#D5110E","#fffdd0","#413E42","#000000","#FF73CE"]
    pixels =     [[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0]]
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,1,1,1,1,1,1,1,0,0,0,0])
    pixels.append([0,0,0,0,0,2,2,2,2,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,4,2,4,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,2,2,2,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,5,5,5,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,0,2,2,2,0,0,0,0,0,0])
    pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0,0])
    pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0,0])
    pixels.append([0,0,0,1,3,3,3,3,3,3,3,1,0,0,0])
    pixels.append([0,0,0,2,3,3,3,3,3,3,3,3,3,0,0])
    pixels.append([0,0,0,0,3,3,3,3,3,3,3,0,0,0,0])
    pixels.append([0,0,0,0,0,1,3,1,1,3,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,4,4,0,4,4,0,0,0,0,0])
    pixels.append([0,0,0,0,0,4,4,0,4,4,0,0,0,0,0])

    for i in range (0,len(pixels)):
        for j in range (0,len(pixels[i])):
                                    t.color(colours[pixels[i][j]])
                                    PixelBox(boxSize)
                                    t.penup()
                                    t.forward(boxSize)
                                    t.pendown()
                                    
        t.setheading(270) 
        t.penup()
        t.forward(boxSize)
        t.setheading(180) 
        t.forward(boxSize*len(pixels[i]))
        t.setheading(0)
        t.pendown()

    t.update()

def Missle_Red():
    #       White       Red     Cream       Grey    Black       Pink
    colours=["#ffffff","#D5110E","#fffdd0","#413E42","#000000","#FF73CE"]
    pixels =     [[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0]]
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,1,1,1,1,1,1,1,0,0,0,0])
    pixels.append([0,0,0,0,0,2,2,2,2,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,4,2,4,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,2,2,2,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,2,5,5,5,2,0,0,0,0,0])
    pixels.append([0,0,0,0,0,0,2,2,2,0,0,0,0,0,0])
    pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0,0])
    pixels.append([0,0,0,1,1,1,1,1,1,1,1,1,0,0,0])
    pixels.append([0,0,0,1,0,1,1,1,1,1,0,1,0,0,0])
    pixels.append([0,0,0,2,0,1,1,1,1,1,0,2,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,1,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,1,1,0,1,1,0,0,0,0,0])
    pixels.append([0,0,0,0,0,4,4,0,4,4,0,0,0,0,0])
    pixels.append([0,0,0,0,0,4,4,0,4,4,0,0,0,0,0])

    for i in range (0,len(pixels)):
        for j in range (0,len(pixels[i])):
                                    t.color(colours[pixels[i][j]])
                                    PixelBox(boxSize)
                                    t.penup()
                                    t.forward(boxSize)
                                    t.pendown()
                                    
        t.setheading(270) 
        t.penup()
        t.forward(boxSize)
        t.setheading(180) 
        t.forward(boxSize*len(pixels[i]))
        t.setheading(0)
        t.pendown()

    t.update()
Missle_Red()
