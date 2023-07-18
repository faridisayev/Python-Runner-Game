import pygame, sys

# start pygame 

pygame.init()

# display surface

screen = pygame.display.set_mode((800, 400))

# set title for a window

pygame.display.set_caption('Runner')

# initialize clock to control framerate

clock = pygame.time.Clock()

# create a font surface 

test_front = pygame.font.Font('./font/Pixeltype.ttf', 50)

# create surfaces

sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()

ground_surface = pygame.image.load('./graphics/Ground.png').convert_alpha()

# create a text surface 

text_surface = test_front.render('My game', False, 'Black')

# create a snail surface and rectangle

snail_surface = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()

snail_rectangle = snail_surface.get_rect(bottomright = (600, 300))

# create player surface and rectangle

player_surface = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()

player_rectangle = player_surface.get_rect(midbottom = (80, 300))

# infinite loop to keep display running 

while True:

    # check for event

    for event in pygame.event.get():

        # check for quit

        if event.type == pygame.QUIT:

            # quit the game 

            pygame.quit()

            # secure exit

            sys.exit()

    # attach surfaces

    screen.blit(sky_surface, (0, 0))

    screen.blit(ground_surface, (0, 300))

    screen.blit(text_surface, (300, 50))

    # move snail farther to the left

    snail_rectangle.x -= 4

    if snail_rectangle.right <= 0:
        snail_rectangle.left = 800

    screen.blit(snail_surface, snail_rectangle)

    # put player 

    screen.blit(player_surface, player_rectangle)

    # update frame

    pygame.display.update()

    # while loop will not run more than 60 times per seconds

    clock.tick(60)