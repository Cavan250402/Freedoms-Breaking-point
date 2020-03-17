from PIL import Image
import os






#Creating Images

# has to have r infront of the C or to have two \ for the file to open
# It turns it from raw code so that it can now be opened as a file directory
RedInfantry = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\InfantryRed.gif")
# Resizing the Image
NewRedInfantry = RedInfantry.resize((20,20))
#Showing the resized image to check 
#NewRedInfantry.show()
#Saving the new image
NewRedInfantry.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\InfantryRedV20.gif")

RedAntiAirMissleLauncher = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\AntiAirMissleLauncherRed.gif")
# Resizing the Image
NewRedAntiAirMissleLauncher = RedAntiAirMissleLauncher.resize((20,20))
#Showing the resized image to check 
#NewRedAntiAirMissleLauncher.show()
#Saving the new image
NewRedAntiAirMissleLauncher.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\AntiAirMissleLauncherRedV20.gif")

RedAntiAirTank = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\AntiAirTankRed.gif")
# Resizing the Image
NewRedAntiAirTank = RedAntiAirTank.resize((20,20))
#Showing the resized image to check 
#NewRedAntiAirTank.show()
#Saving the new image
NewRedAntiAirTank.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\AntiAirTankRedV20.gif")


RedBomber = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\BomberRed.gif")
# Resizing the Image
NewRedBomber = RedBomber.resize((20,20))
#Showing the resized image to check 
#NewRedBomber.show()
#Saving the new image
NewRedBomber.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\BomberRedV20.gif")

RedHelicopter = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\HelicopterRed.gif")
# Resizing the Image
NewRedHelicopter = RedHelicopter.resize((20,20))
#Showing the resized image to check 
#NewRedHelicopter.show()
#Saving the new image
NewRedHelicopter.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\HelicopterRedV20.gif")

RedJeep = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\JeepRed.gif")
# Resizing the Image
NewRedJeep = RedJeep.resize((20,20))
#Showing the resized image to check 
#NewRedJeep.show()
#Saving the new image
NewRedJeep.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\JeepRedV20.gif")

RedMobileGun = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\MobileGunRed.gif")
# Resizing the Image
NewRedMobileGun = RedMobileGun.resize((20,20))
#Showing the resized image to check 
#NewRedMobileGun.show()
#Saving the new image
NewRedMobileGun.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\MobileGunRedV20.gif")

RedRocketLauncher = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\RocketLauncherRed.gif")
# Resizing the Image
NewRedRocketLauncher = RedRocketLauncher.resize((20,20))
#Showing the resized image to check 
#NewRedRocketLauncher.show()
#Saving the new image
NewRedRocketLauncher.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\RocketLauncherRedV20.gif")

RedTank = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\TankRed.gif")
# Resizing the Image
NewRedTank = RedTank.resize((20,20))
#Showing the resized image to check 
#NewRedTank.show()
#Saving the new image
NewRedTank.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\TankRedV20.gif")

RedTransporter = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\TransporterRed.gif")
# Resizing the Image
NewRedTransporter = RedTransporter.resize((20,20))
#Showing the resized image to check 
#NewRedTransporter.show()
#Saving the new image
NewRedTransporter.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\TransporterRedV20.gif")

# Blue Team




BlueInfantry = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\InfantryBlue.gif")
# Resizing the Image
NewBlueInfantry = BlueInfantry.resize((20,20))
#Flipping the image
NewBlueInfantryV2 = NewBlueInfantry.transpose(Image.FLIP_LEFT_RIGHT)
#Showing the resized image to check 
NewBlueInfantry.show()
#Saving the new image
NewBlueInfantry.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\InfantryBlueV20.gif")

BlueAntiAirMissleLauncher = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\AntiAirMissleLauncherBlue.gif")
# Resizing the Image
NewBlueAntiAirMissleLauncher = BlueAntiAirMissleLauncher.resize((20,20))
#Showing the resized image to check 
NewBlueAntiAirMissleLauncher.show()
#Saving the new image
NewBlueAntiAirMissleLauncher.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\AntiAirMissleLauncherBlueV20.gif")

BlueAntiAirTank = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\AntiAirTankBlue.gif")
# Resizing the Image
NewBlueAntiAirTank = BlueAntiAirTank.resize((20,20))
#Showing the resized image to check 
NewBlueAntiAirTank.show()
#Saving the new image
NewBlueAntiAirTank.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\AntiAirTankBlueV20.gif")


BlueBomber = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\BomberBlue.gif")
# Resizing the Image
NewBlueBomber = BlueBomber.resize((20,20))
#Showing the resized image to check 
NewBlueBomber.show()
#Saving the new image
NewBlueBomber.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\BomberBlueV20.gif")

BlueHelicopter = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\HelicopterBlue.gif")
# Resizing the Image
NewBlueHelicopter = BlueHelicopter.resize((20,20))
#Showing the resized image to check 
NewBlueHelicopter.show()
#Saving the new image
NewBlueHelicopter.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\HelicopterBlueV20.gif")

BlueJeep = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\JeepBlue.gif")
# Resizing the Image
NewBlueJeep = BlueJeep.resize((20,20))
#Showing the resized image to check 
NewBlueJeep.show()
#Saving the new image
NewBlueJeep.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\JeepBlueV20.gif")

BlueMobileGun = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\MobileGunBlue.gif")
# Resizing the Image
NewBlueMobileGun = BlueMobileGun.resize((20,20))
#Showing the resized image to check 
NewBlueMobileGun.show()
#Saving the new image
NewBlueMobileGun.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\MobileGunBlueV20.gif")

BlueRocketLauncher = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\RocketLauncherBlue.gif")
# Resizing the Image
NewBlueRocketLauncher = BlueRocketLauncher.resize((20,20))
#Showing the resized image to check 
NewBlueRocketLauncher.show()
#Saving the new image
NewBlueRocketLauncher.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\RocketLauncherBlueV20.gif")

BlueTank = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\TankBlue.gif")
# Resizing the Image
NewBlueTank = BlueTank.resize((20,20))
#Showing the resized image to check 
NewBlueTank.show()
#Saving the new image
NewBlueTank.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\TankBlueV20.gif")

BlueTransporter = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\TransporterBlue.gif")
# Resizing the Image
NewBlueTransporter = BlueTransporter.resize((20,20))
#Showing the resized image to check 
NewBlueTransporter.show()
#Saving the new image
NewBlueTransporter.save("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Blue team\\TransporterBlueV20.gif")

