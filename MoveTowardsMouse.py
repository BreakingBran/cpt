# Define colors, and constants
RED = (255,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
YELLOW = (239,255,0)
DARK_BLUE = (7,32,133)
DARK_GREEN = (6,59,9)
LIGHT_GREY = (224,224,224)
WATER_BLUE = (63,31,222)
BROWN = (133,69,69)
SCREEN_SIZE = (1100,500)


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Testing AND Stuff number 2")
clock = pygame.time.Clock()


def main():
    done = False
    playerPos = [SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2]
    background_image = pygame.image.load("Images and Sounds/lilycove_city_e.png").convert()
    player_image = pygame.image.load("Images and Sounds/rayquaza.png").convert()
    player_image.set_colorkey(WHITE)
    click_sound = pygame.mixer.Sound("R:\STFXS\ICS3U1-04-STFXS\Students\Pereira, Lance\Sounds\laser5.ogg")
    x_speed = 0
    y_speed = 0
    while not done:
        clock.tick(20)
        for event in pygame.event.get(
