import pygame, sys
from random import randint

# display score function 

def display_score():

    current_time = int(pygame.time.get_ticks() / 1000) - start_time

    score_surface = text_font.render(f'Score: {current_time}', False, (64, 64, 64, 64))

    score_rectangle = score_surface.get_rect(center = (400, 50))

    screen.blit(score_surface, score_rectangle)

    return current_time

# obstacle movement 

def obstacle_movement(obstacle_list):

    if obstacle_list:

        for obstacle_rect in obstacle_list:

            obstacle_rect.x -= 5

            if obstacle_rect.bottom == 300:

                screen.blit(snail_surface, obstacle_rect)

            else:

                screen.blit(fly_surface, obstacle_rect)

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]

        return obstacle_list
    
    else:

        return []
    
# collisions 

def collisions(player, obstacles):

    if obstacles:

        for obstacle_rect in obstacles:

            if player.colliderect(obstacle_rect):

                return False
            
    return True

# player animation 

def player_animation():

    global player_surface, player_index

    if player_rectangle.bottom < 300:
        
        player_surface = player_jump

    else:

        player_index += 0.1

        if player_index >= len(player_walk):

            player_index = 0

        player_surface = player_walk[int(player_index)]

# start pygame 

pygame.init()

# display surface

screen = pygame.display.set_mode((800, 400))

# set title for a window

pygame.display.set_caption('Runner')

# initialize clock to control framerate

clock = pygame.time.Clock()

# create sky and ground surfaces

sky_surface = pygame.image.load('./graphics/Sky.png').convert_alpha()

ground_surface = pygame.image.load('./graphics/Ground.png').convert_alpha()

# create a font surface 

text_font = pygame.font.Font('./font/Pixeltype.ttf', 50)

# create player surface and rectangle

player_walk_1 = pygame.image.load('./graphics/player/player_walk_1.png').convert_alpha()

player_walk_2 = pygame.image.load('./graphics/player/player_walk_2.png').convert_alpha()

player_walk = [player_walk_1, player_walk_2]

player_index = 0

player_jump = pygame.image.load('./graphics/player/jump.png').convert_alpha()

player_surface = player_walk[player_index]

player_rectangle = player_surface.get_rect(midbottom = (80, 300))

# Intro screen

player_stand = pygame.image.load('./graphics/player/player_stand.png').convert_alpha()

player_stand= pygame.transform.rotozoom(player_stand, 0, 2)

player_stand_rectangle = player_stand.get_rect(center = (400, 200))

game_name = text_font.render('Pixel Runner', False, (111, 196, 169))

game_name_rectangle = game_name.get_rect(center = (400, 80))

# messages 

game_message = text_font.render('Press space to run', False, (111, 196, 169))

game_message_rectangle = game_message.get_rect(center = (400, 320))

# track gravity 

player_gravity = 0

# activate game 

game_active = False

# start time counter 

start_time = 0

# set score 

score = 0

# obstacles 

snail_frame_1 = pygame.image.load('./graphics/snail/snail1.png').convert_alpha()

snail_frame_2 = pygame.image.load('./graphics/snail/snail2.png').convert_alpha()

snail_frames = [snail_frame_1, snail_frame_2]

snail_frame_index = 0

snail_surface = snail_frames[snail_frame_index]

fly_frame_1 = pygame.image.load('./graphics/fly/fly1.png').convert_alpha()

fly_frame_2 = pygame.image.load('./graphics/fly/fly2.png').convert_alpha()

fly_frames = [fly_frame_1, fly_frame_2]

fly_frame_index = 0

fly_surface = fly_frames[fly_frame_index]

obstacle_rect_list = []

# set obstacle timer

obstacle_timer = pygame.USEREVENT + 1

pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2

pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3

pygame.time.set_timer(fly_animation_timer, 200)

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

        if game_active:

            # check for keyup, keydown 

            if event.type == pygame.KEYDOWN:

                # check if space is pressed 

                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 300:

                    # decrease gravity

                    player_gravity = -20

            # check for mouse position

            if event.type == pygame.MOUSEBUTTONDOWN:

                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 300:
                    
                    # decrease gravity 

                    player_gravity = -20

        else:

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:

                game_active = True

                start_time = int(pygame.time.get_ticks() / 1000)

        if game_active:

            if event.type == obstacle_timer:

                if randint(0, 2):

                    obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))

                else:

                    obstacle_rect_list.append(fly_surface.get_rect(bottomright = (randint(900, 1100), 210)))

            if event.type == snail_animation_timer:

                if snail_frame_index == 0:
                    
                    snail_frame_index = 1

                else:

                    snail_frame_index = 0

                snail_surface = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:

                if fly_frame_index == 0:

                    fly_frame_index = 1

                else:

                    fly_frame_index = 0

                fly_surface = fly_frames[fly_frame_index]
        
    if game_active:

        # attach surfaces

        screen.blit(sky_surface, (0, 0))

        screen.blit(ground_surface, (0, 300))

        # get the score 

        score = display_score()

        display_score()

        # player

        player_gravity += 1

        player_rectangle.y += player_gravity

        if player_rectangle.bottom > 300:

            player_rectangle.bottom = 300

        # manage player animation 

        player_animation()

        screen.blit(player_surface, player_rectangle)

        # obstacle movement

        ibstacle_rect_list = obstacle_movement(obstacle_rect_list)

        # collision 

        game_active = collisions(player_rectangle, obstacle_rect_list)

    else:

        screen.fill((94, 129, 162))

        # manage player and obstacle position

        screen.blit(player_stand, player_stand_rectangle)

        screen.blit(game_name, game_name_rectangle)

        obstacle_rect_list.clear()

        player_rectangle.midbottom = (80, 300)

        player_gravity = 0

        # score 

        score_message = text_font.render(f'Your score: {score}', False, (111, 196, 169))

        score_message_rectangle = score_message.get_rect(center = (400, 330))

        if score == 0:

            screen.blit(game_message, game_message_rectangle)

        else:

            screen.blit(score_message, score_message_rectangle)

    # update frame

    pygame.display.update()

    # while loop will not run more than 60 times per second

    clock.tick(60)
