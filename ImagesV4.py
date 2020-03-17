from turtle import Screen, Turtle
from SquareV2 import *
screen = Screen()
screen.tracer(False)


# Assiging the images to variables

RedInfantry = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\InfantryRedV20.gif"
BlueInfantry = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\InfantryBlueV20.gif"
RedTank = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\TankRedV20.gif"
BlueTank = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\TankBlueV20.gif"
RedMobileGun = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\MobileGunRedV20.gif"
BlueMobileGun = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\MobileGunBlueV20.gif"
RedRocketLauncher = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\RocketLauncherRedV20.gif"
BlueRocketLauncher = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\RocketLauncherBlueV20.gif"
RedAntiAirTank = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\AntiAirTankRedV20.gif"
BlueAntiAirTank = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\AntiAirTankBlueV20.gif"
RedSupplyTruck = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\TransporterRedV20.gif"
BlueSupplyTruck = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\TransporterBlueV20.gif"
RedAntiAirMissleLauncher = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\AntiAirMissleLauncherRedV20.gif"
BlueAntiAirMissleLauncher = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\AntiAirMissleLauncherBlueV20.gif"
RedHelicopter = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\HelicopterRedV20.gif"
BlueHelicopter = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\HelicopterBlueV20.gif"
RedBomber = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\BomberRedV20.gif"
BlueBomber = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\BomberBlueV20.gif"
RedJeep = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Red team\JeepRedV20.gif"
BlueJeep = r"C:\Users\User\Desktop\a level computer science\Coursework\Week\Blue team\JeepBlueV20.gif"

#Adding the red team
screen.addshape(RedAntiAirMissleLauncher)
screen.addshape(RedAntiAirTank)
screen.addshape(RedBomber)
screen.addshape(RedHelicopter)
screen.addshape(RedInfantry)
screen.addshape(RedJeep)
screen.addshape(RedMobileGun)
screen.addshape(RedRocketLauncher)
screen.addshape(RedSupplyTruck)
screen.addshape(RedTank)
screen.addshape(BlueAntiAirMissleLauncher)
screen.addshape(BlueAntiAirTank)
screen.addshape(BlueBomber)
screen.addshape(BlueHelicopter)
screen.addshape(BlueInfantry)
screen.addshape(BlueJeep)
screen.addshape(BlueMobileGun)
screen.addshape(BlueRocketLauncher)
screen.addshape(BlueSupplyTruck)
screen.addshape(BlueTank)

#Red Infantry
def InfantryRed(x, y):
    turtle = Turtle()
    turtle.shape(RedInfantry)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 0
    Attack = 1
    Movement = 2
    Capture = True

    return turtle


#Blue Infantry
def InfantryBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueInfantry)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 0
    Attack = 1
    Movement = 2
    Capture = True

    return turtle
#Red Tank
def TankRed(x,y):
    turtle = Turtle()
    turtle.shape(RedTank)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 2
    Attack = 4
    Movement = 5
    Capture = False

    return turtle
#Blue Tank
def TankBlue(x,y):
    
    turtle = Turtle()
    turtle.shape(BlueTank)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 2
    Attack = 4
    Movement = 5
    Capture = False

    return turtle
#Red mobileGun
def MobileGunRed(x,y):
    turtle = Turtle()
    turtle.shape(RedMobileGun)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 4
    Movement = 1
    Capture = False
    
    return turtle

#Blue Mobile gun
def MobileGunBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueMobileGun)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 4
    Movement = 1
    Capture = False

    return turtle
#Red Rocket Launcher
def RocketLauncherRed(x,y):
    turtle = Turtle()
    turtle.shape(RedRocketLauncher)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 2
    Attack = 3
    Movement = 3
    Capture = False
    
    return turtle
#Blue Rocket Launcher
def RocketLauncherBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueRocketLauncher)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 2
    Attack = 3
    Movement = 3
    Capture = False
    
    return turtle
#Red AntiAirTank
def AntiAirTankRed(x,y):
    turtle = Turtle()
    turtle.shape(RedAntiAirTank)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 2
    Movement = 5
    Capture = False
    
    return turtle
#Blue AntiAirTank
def AntiAirTankBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueAntiAirTank)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 2
    Movement = 5
    Capture = False
    
    return turtle
#Red Supply Truck
def SupplyTruckRed(x,y):
    turtle = Turtle()
    turtle.shape(RedSupplyTruck)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 3
    Attack = 0
    Movement = 4
    Capture = False
    return turtle

#Blue supply Truck
def SupplyTruckBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueSupplyTruck)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 3
    Attack = 0
    Movement = 4
    Capture = False
    
    return turtle
#Red Anti Air Missle Truck
def AntiAirMissleLauncherRed(x,y):
    turtle = Turtle()
    turtle.shape(RedAntiAirMissleLauncher)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 4
    Movement = 2
    Capture = False

    return turtle
#Blue Anti Aie Missle Truck
def AntiAirMissleLauncherBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueAntiAirMissleLauncher)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 4
    Movement = 2
    Capture = False


    return turtle

#Red Helicopter
def HelicopterRed(x,y):
    turtle = Turtle()
    turtle.shape(RedHelicopter)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 4
    Movement = 3
    Capture = False

    return turtle
#Blue Helicopter
def HelicopterBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueHelicopter)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 3
    Movement = 6
    Capture = False

    return turtle
#Red Bomber
def BomberRed(x,y):
    turtle = Turtle()
    turtle.shape(RedBomber)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 5
    Movement = 7
    Capture = False

    return turtle
#Blue Bomber
def BomberBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueBomber)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 5
    Movement = 7
    Capture = False

    return turtle
#Red Jeep
def JeepRed(x,y):
    turtle = Turtle()
    turtle.shape(RedJeep)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 2
    Movement = 5
    Capture = False

    return turtle

#Blue Jeep
def JeepBlue(x,y):
    turtle = Turtle()
    turtle.shape(BlueJeep)
    turtle.penup()
    turtle.goto(x, y)
    Health = 10
    Armour = 1
    Attack = 2
    Movement = 5
    Capture = False

    return turtle

#Square(25,"green")
#infantry_1 = InfantryBlue(12.5, -12.5)
#infantry_2 = InfantryRed(-200, 200)
#infantry_3 = InfantryRed(-200, -200)

#infantry_1.goto(200, 200)

screen.update()
screen.exitonclick()
