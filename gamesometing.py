import pygame
from pygame.locals import *

#define FPS
clock = pygame.time.Clock()
fps = 60


screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invaders')


#load image
bg = pygame.image.load("img/bg.png")

def draw_bg():
    screen.blit(bg, (0,0))


#create space ship class

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("img/spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

#create sprite groups
spaceship_group = pygame.sprite.Group()


#create player 
spaceship = Spaceship(int(screen_width / 2), screen_height - 100)
spaceship_group.add(spaceship)



run = True
while run:

    clock.tick(fps)

    #draw backroud
    draw_bg()

    #event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update sprite groups
    spaceship_group.draw(screen)
    

    pygame.display.update()

pygame.quit()