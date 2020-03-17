from PIL import Image
import os

size_20 = (20,20)
#making all the images 20,20

for f in os.listdir("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team"):
    if f.endswith('.gif'):
        i = Image.open(f)
        fn, fext = os.path.splitext(f)

        i.thumbnail(size_20)
        i.save('20/{}_20{}'.format(fn, fext))


#Creating Images

# has to have r infront of the C or to have two \ for the file to open
# It turns it from raw code so that it can now be opened as a file directory
#RedInfantry = Image.open("C:\\Users\\User\\Desktop\\a level computer science\\Coursework\\Week\\Red team\\InfantryRed.gif")
#RedInfantry.show()
