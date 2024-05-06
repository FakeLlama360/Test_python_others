import pygame
from pygame.locals import *


screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')


#load image
bg = pygame.image.load("")

run = True
while run:

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()