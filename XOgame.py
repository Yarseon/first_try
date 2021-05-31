import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


line(screen, 90, (150, 50), (150, 350), 5)
line(screen, 90, (250, 50), (250, 350), 5)
line(screen, 90, (50, 150), (350, 150), 10)
line(screen, 90, (50, 250), (350, 250), 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()