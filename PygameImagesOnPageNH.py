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


Active = False 


def SetUp():
        # draw scene

    grid[0][2] = RedInfantry
    grid[2][2] = RedAntiAirMissleLauncher
    grid[4][2] = RedAntiAirTank
    grid[6][2] = RedBomber
    grid[8][2] = RedHelicopter
    grid[10][2] = RedJeep
    grid[12][2] = RedMobileGun
    grid[2][4] = RedRocketLauncher
    grid[4][4] = RedTank
    grid[6][4] = RedTransporter
    grid[0][9] = BlueInfantry
    grid[2][9] = BlueAntiAirMissleLauncher
    grid[4][9] = BlueAntiAirTank
    grid[6][9] = BlueBomber
    grid[8][9] = BlueHelicopter
    grid[10][9] = BlueJeep
    grid[12][9] = BlueMobileGun
    grid[2][11] = BlueRocketLauncher
    grid[4][11] = BlueTank
    grid[6][11] = BlueTransporter
    
    for i in range(0, 900, 50):
        pygame.draw.line(Background, (0, 0, 0), (0, i), (900, i))
        pygame.draw.line(Background, (0, 0, 0), (i, 0), (i, 900))
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            x = i * 50
            y = j * 50
            image = grid[i][j]
            if image == RedInfantry:
                Background.blit(RedInfantry,(x, y))
            elif image == BlueInfantry:
                Background.blit(BlueInfantry,(x, y))
            elif image == RedAntiAirMissleLauncher:
                Background.blit(RedAntiAirMissleLauncher,(x,y))
            elif image == BlueAntiAirMissleLauncher:
                Background.blit(BlueAntiAirMissleLauncher,(x,y))
            elif image == RedAntiAirTank:
                Background.blit(RedAntiAirTank,(x,y))
            elif image == BlueAntiAirTank:
                Background.blit(BlueAntiAirTank,(x,y))
            elif image == RedBomber:
                Background.blit(RedBomber,(x,y))
            elif image == BlueBomber:
                Background.blit(BlueBomber,(x,y))
            elif image == RedHelicopter:
                Background.blit(RedHelicopter,(x,y))
            elif image == BlueHelicopter:
                Background.blit(BlueHelicopter,(x,y))
            elif image == RedJeep:
                Background.blit(RedJeep,(x,y))
            elif image == BlueJeep:
                Background.blit(BlueJeep,(x,y))
            elif image == RedMobileGun:
                Background.blit(RedMobileGun,(x,y))
            elif image == BlueMobileGun:
                Background.blit(BlueMobileGun,(x,y))
            elif image == RedRocketLauncher:
                Background.blit(RedRocketLauncher,(x,y))
            elif image == BlueRocketLauncher:
                Background.blit(BlueRocketLauncher,(x,y))
            elif image == RedTank:
                Background.blit(RedTank,(x,y))
            elif image == BlueTank:
                Background.blit(BlueTank,(x,y))
            elif image == RedTransporter:
                Background.blit(RedTransporter,(x,y))
            elif image == BlueTransporter:
                Background.blit(BlueTransporter,(x,y))

RedUnits = [[RedInfantry,False],[RedAntiAirMissleLauncher,False]]
            
Background.fill(Green)

SetUp()

pygame.display.update()


run = True
while run:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Background.blit(RedInfantry,(50, 50))

            
        



    # draw background


                

    # update dispaly
    pygame.display.update()
