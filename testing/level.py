'''
Always Face Mouse
'''
# 
# http://stackoverflow.com/questions/20162302/pygame-point-image-towards-mouse

import pygame, random, math
from pygame import *

# Goal is to make a level generator

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

                # Width and height of character
		self.width = 40
		self.height = 40
		self.image = pygame.Surface([self.width,self.height])
		self.image.fill(red)
		self.image.set_colorkey(red)

                # Draw rectangle as character on screen
                pygame.draw.rect(self.image,white,[0,0,self.width,self.height])

                # Get rect frame
                self.rect = self.image.get_rect()

                # angle to face mouse
                self.angle = 0

        def update(self):

                # WIP set pygame.rotate ??? 
                self.rotate = 

pygame.init()

# dimentions of screen
width = 300
height = 300

# COLORS 
bg = (0,0,0)
white = (255,255,255)
red = (255,0,0)

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

# LOOP
done = False

while not done:
        # Quit pygame
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        screen.fill(bg)

        # Get mouse cords while game running
        pos = pygame.mouse.get_pos()

        #print (pos)

        # WIP get angle from mouse and player
        Player.angle, mouse_angle = 360-math.atan2(pos[1]-300,pos[0]-300)*180/math.pi

        # Call update function of sprites
        all_sprites_list.update()

        # Draw all sprites on screen
        all_sprites_list.draw(screen)

        # Set tick rate to 60
        clock.tick(60)

        # Redraw screen
        pygame.display.flip()


# Quit if loop is exited
pygame.quit()
