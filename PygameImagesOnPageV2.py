import pygame 
pygame.init()

Background = pygame.display.set_mode((900 ,900))
Green = (45,198,14)

RedInfantry = pygame.image.load("InfantryRedV20.gif")
RedAntiAirMissleLauncher = pygame.image.load("AntiAirMissleLauncherRedV20.gif")
RedAntiAirTank = pygame.image.load("AntiAirTankRedV20.gif")
RedBomber = pygame.image.load("BomberRedV20.gif")
RedHelicopter = pygame.image.load("HelicopterRedV20.gif")
RedJeep = pygame.image.load("JeepRedV20.gif")
RedMobileGun = pygame.image.load("MobileGunRedV20.gif")
RedRocketLauncher = pygame.image.load("RocketLauncherRedV20.gif")
RedTank = pygame.image.load("TankRedV20.gif")
RedTransporter = pygame.image.load("TransporterRedV20.gif")

BlueInfantry = pygame.image.load("InfantryBlueV20.gif")
BlueAntiAirMissleLauncher = pygame.image.load("AntiAirMissleLauncherBlueV20.gif")
BlueAntiAirTank = pygame.image.load("AntiAirTankBlueV20.gif")
BlueBomber = pygame.image.load("BomberBlueV20.gif")
BlueHelicopter = pygame.image.load("HelicopterBlueV20.gif")
BlueJeep = pygame.image.load("JeepBlueV20.gif")
BlueMobileGun = pygame.image.load("MobileGunBlueV20.gif")
BlueRocketLauncher = pygame.image.load("RocketLauncherBlueV20.gif")
BlueTank = pygame.image.load("TankBlueV20.gif")
BlueTransporter = pygame.image.load("TransporterBlueV20.gif")


grid = [[None for i in range(0, 900, 50)] for j in range(0, 900, 50)]
grid[0][2] = RedInfantry
grid[1][2] = RedAntiAirMissleLauncher
grid[2][2] = RedAntiAirTank
grid[3][2] = RedBomber
grid[4][2] = RedHelicopter
grid[5][2] = RedJeep
grid[6][2] = RedMobileGun
grid[7][2] = RedRocketLauncher
grid[8][2] = RedTank
grid[9][2] = RedTransporter

grid[0][9] = BlueInfantry
grid[1][9] = BlueAntiAirMissleLauncher
grid[2][9] = BlueAntiAirTank
grid[3][9] = BlueBomber
grid[4][9] = BlueHelicopter
grid[5][9] = BlueJeep
grid[6][9] = BlueMobileGun
grid[7][9] = BlueRocketLauncher
grid[8][9] = BlueTank
grid[9][9] = BlueTransporter



run = True
while run:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # draw background
    Background.fill(Green)

    # draw scene
    for i in range(0, 900, 50):
        pygame.draw.line(Background, (0, 0, 0), (0, i), (900, i))
        pygame.draw.line(Background, (0, 0, 0), (i, 0), (i, 900))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x, y = i * 50, j * 50
            image = grid[i][j]
            if image != None:
                Background.blit(RedInfantry,(x, y))
                Background.blit(BlueInfantry,(x, y))


            

    # update dispaly
    pygame.display.update()
