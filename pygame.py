import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 255), (200, 175), 100, 2)
circle(screen, (255, 255, 255), (260, 155), 15, 2)
circle(screen, (255, 255, 255), (150, 155), 20, 2)
line(screen, 100, (190, 150), (110, 110), 10)
line(screen, 90, (290, 120), (220, 140), 10)
line(screen, 90, (130, 220), (270, 210), 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()