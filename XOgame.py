import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


line(screen, 90, (130, 110), (130, 300), 5)
line(screen, 90, (250, 110), (250, 300), 5)
line(screen, 90, (100, 150), (300, 150), 10)
line(screen, 90, (100, 250), (300, 250), 10)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()