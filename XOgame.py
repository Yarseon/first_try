import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))


line(screen, 90, (150, 50), (150, 350), 5)
line(screen, 90, (250, 50), (250, 350), 5)
line(screen, 90, (50, 150), (350, 150), 10)
line(screen, 90, (50, 250), (350, 250), 10)

onelane1 = 160
secondlane1 = 240

def draw_X_North():
    line(screen, 90, (onelane1, onelane1-100), (secondlane1, secondlane1-100), 5)
    line(screen, 90, (onelane1, secondlane1-100), (secondlane1, onelane1-100), 5)

def draw_X_mid():
    line(screen, 90, (onelane1, onelane1), (secondlane1, secondlane1), 5)
    line(screen, 90, (secondlane1, onelane1), (onelane1, secondlane1), 5)

def draw_X_South():
    line(screen, 90, (onelane1, onelane1+100), (secondlane1, secondlane1+100), 5)
    line(screen, 90, (onelane1, secondlane1+100), (secondlane1, onelane1+100), 5)

def draw_X_Left():
    line(screen, 90, (onelane1-100, onelane1), (secondlane1-100, secondlane1), 5)
    line(screen, 90, (onelane1-100, secondlane1), (secondlane1-100, onelane1), 5)

def draw_X_Right():
    line(screen, 90, (onelane1+100, onelane1), (secondlane1+100, secondlane1), 5)
    line(screen, 90, (onelane1+100, secondlane1), (secondlane1+100, onelane1), 5)

def draw_X_Right_North():
    line(screen, 90, (onelane1 + 100, onelane1-100), (secondlane1 + 100, secondlane1-100), 5)
    line(screen, 90, (onelane1 + 100, secondlane1-100), (secondlane1 + 100, onelane1-100), 5)

def draw_X_Right_South():
    line(screen, 90, (onelane1 + 100, onelane1+100), (secondlane1 + 100, secondlane1+100), 5)
    line(screen, 90, (onelane1 + 100, secondlane1+100), (secondlane1 + 100, onelane1+100), 5)

def draw_X_Left_South():
    line(screen, 90, (onelane1 - 100, onelane1 + 100), (secondlane1 - 100, secondlane1 + 100), 5)
    line(screen, 90, (onelane1 - 100, secondlane1 + 100), (secondlane1 - 100, onelane1 + 100), 5)

def draw_X_Left_North():
    line(screen, 90, (onelane1 - 100, onelane1 - 100), (secondlane1 - 100, secondlane1 - 100), 5)
    line(screen, 90, (onelane1 - 100, secondlane1 - 100), (secondlane1 - 100, onelane1 - 100), 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()