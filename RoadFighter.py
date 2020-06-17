import math
import random
import pygame
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Road Fighter - [YYSCOOP.com]")
favicon = pygame.image.load("img/favicon.ico")
pygame.display.set_icon(favicon)

game_background = pygame.image.load("img/background_road_800_600.png")

mixer.music.load("src/background_music.mp3")
mixer.music.play(-1)

# mixer.Sound("src/collision_sound.wav").play()
# collision_sound = mixer.Sound("src/collision_sound.wav")
# collision_sound.play()

## Player
player_image = pygame.image.load("img/player_car_50_75.png")
player_xpos = 280
player_ypos = 510
player_xmove = 0

##Traffic
traffic_image = []
traffic_xpos = []
traffic_ypos = []
# traffic_xmove = []
traffic_ymove = []
total_traffic = 5    ## Setting total traffic car
traffic_speed = 7
for traffic_id in range(total_traffic):
    traffic_image.append(pygame.image.load("img/traffic_car_64_64.png"))
    traffic_xpos.append(random.randint(220,510))
    traffic_ypos.append(random.randint(-600, 5))
    traffic_ymove.append(traffic_speed)

## score
score = 0
score_xpos = 1
score_ypos = 1
score_font = pygame.font.Font("freesansbold.ttf",32)

## Gameover
gameover_font = pygame.font.Font("freesansbold.ttf",60)
## collision
collision_status = False
collision_count = 0

def set_player(xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    screen.blit(player_image,(xvalue, yvalue))

def set_traffic(image,xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    screen.blit(image, (xvalue, yvalue))

def set_score(xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    score_text = score_font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_text,(xvalue,yvalue))

def set_gameover():
    gameover_text = gameover_font.render("GAME OVER",True,(0,0,0))
    screen.blit(gameover_text,(215,270))

def detect_collision(p_xvalue,p_yvalue,t_xvalue,t_yvalue):
    global collision_status
    collision_value = math.sqrt(math.pow(p_xvalue-t_xvalue,2) + math.pow(p_yvalue-t_yvalue,2))
    # print(collision_value)
    if collision_value <= 55:
        collision_status = True

## Main Game Loop -------------------------------
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(game_background,(0,0))

    ## Setting Keyboard Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_xmove = 5
            if event.key == pygame.K_LEFT:
                player_xmove = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_RIGHT:
                player_xmove = 0

    ## Updating player & traffic position
    player_xpos = player_xpos + player_xmove

    ## Creating boundaries for player & traffic
    if player_xpos <= 220:
        player_xpos = 220
    if player_xpos >= 530:
        player_xpos = 530
    ## Setting player New position
    set_player(player_xpos,player_ypos)

    ## Updating / creating / setting traffic positions
    for traffic_id in range(total_traffic):
        traffic_ypos[traffic_id] = traffic_ypos[traffic_id] + traffic_ymove[traffic_id]
        if traffic_ypos[traffic_id] >= 600:
            traffic_ypos[traffic_id] = random.randint(-600, 5)
            traffic_xpos[traffic_id] = random.randint(220, 520)
            score += 1
        set_traffic(traffic_image[traffic_id], traffic_xpos[traffic_id], traffic_ypos[traffic_id])

        ## checking traffic collision with player
        detect_collision(player_xpos,player_ypos,traffic_xpos[traffic_id],traffic_ypos[traffic_id])
        if collision_status == True:
            for t_id in range(total_traffic):
                traffic_ymove[t_id]=0        ## Pausing traffic movements
                traffic_speed = 0
            if collision_count == 0:
                collision_sound = mixer.Sound("src/collision_sound.wav")
                collision_sound.play()
                collision_count += 1
            set_gameover()
            break


    ## Setting Score ----------
    set_score(score_xpos, score_ypos)

    pygame.display.update()

