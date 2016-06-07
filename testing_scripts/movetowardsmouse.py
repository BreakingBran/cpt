'''
Move Towards Mouse
'''

import pygame
from pygame import *

import pygame
from pygame import *
from math import *


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Width and height of image
        self.width = 40
        self.height = 40

        # Creates images (CREATE TWO, one for refrence later)
        self.imageMaster = pygame.Surface([self.width,self.height])
        self.image = self.imageMaster

        # Fills the image with white
        self.image.fill(white)

        # Makes transparent background
        # YOU NEED THIS FOR IT TO ROTATE
        self.image.set_colorkey(red)
        
        # Get rect frame of image
        self.rect = self.image.get_rect()

        # angle to face mouse
        self.rect.x = 150
        self.rect.y = 150

        # Just placeholder
        self.angle = 0
        self.vely = 2
        self.velx = 2

    def get_pos(self):
        # Get mouse cords while game running
        self.pos = pygame.mouse.get_pos()

        # Get change in X and y dy/dy
        self.dy = self.pos[1] - self.rect.y
        self.dx = self.pos[0] - self.rect.x

        # Get angle from mouse and player
        self.mouse_angle = atan2(-self.dy,self.dx)
        # Var for move function
        self.angle_move = self.mouse_angle
        self.mouse_angle %= 2*pi
        self.mouse_angle = degrees(self.mouse_angle)

        # Sets angle value in class
        self.angle = self.mouse_angle

    def move(self):
        # WHILE NOT AT MOUSE POS RUN LOOP??
        #self.rect.x +=  cos(self.angle) * abs(self.pos[0] - self.rect.x)
        #self.rect.y +=  sin(self.angle) * abs(self.pos[1] - self.rect.y)
        print self.rect

        # SET VALUE
                
    def update(self):
        
        # Gets mouse position
        self.get_pos()

        # Gets the old center point
        self.centerpoint = self.rect.center

        # Rotate sprite
        self.image = pygame.transform.rotate(self.imageMaster ,self.angle)

        # Get rectangle frame
        self.rect = self.image.get_rect()

        # Sets the new image to the old center point
        # Makes sure the sprite does not go flying to oblivion
        self.rect.center = self.centerpoint
    
pygame.init()

# dimentions of screen
width = 300
height = 300

# COLORS 
bg = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)

# Screen
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("testing mouse and player")

# Create sprite group
all_sprites_list = pygame.sprite.Group()

# Create object player
player = Player()

# Adds player to sprites list
all_sprites_list.add(player)

# Game time for clock functions
clock = pygame.time.Clock()

# Fill background (Makes cicle, when loop screen.fill is commented)
#screen.fill(bg)

# LOOP
done = False

while not done:
            # Quit pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP:
                player.move()

        # Call update function of sprites
        all_sprites_list.update()

        # fills background color
        screen.fill(bg)

        # Draw all sprites on screen
        all_sprites_list.draw(screen)

        # Set tick rate to 60
        clock.tick(60)

        # Redraw screen
        pygame.display.flip()

# Quit if loop is exited
pygame.quit()
