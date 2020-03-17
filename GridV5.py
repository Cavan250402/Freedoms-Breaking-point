import pygame

pygame.init()

Background = pygame.display.set_mode((900 ,900))
Green = (45,198,14)
Background.fill(Green)

for i in range(0, 900, 50):
    pygame.draw.line(Background, (0, 0, 0), (0, i), (900, i))
    pygame.draw.line(Background, (0, 0, 0), (i, 0), (i, 900))
pygame.display.update()

while pygame.event.wait().type != pygame.QUIT:
    pass
