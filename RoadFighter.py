import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Road Fighter - [YYSCOOP.com]")
favicon = pygame.image.load("img/favicon.ico")
pygame.display.set_icon(favicon)

game_background = pygame.image.load("img/background_road_800_600.png")

## Player
player_image = pygame.image.load("img/player_car_50_75.png")
player_xpos = 280
player_ypos = 510
player_xmove = 0

#Traffic
traffic_image = []
traffic_xpos = []
traffic_ypos = []
# traffic_xmove = []
traffic_ymove = []
total_traffic = 5

# score
score = 0
score_xpos = 1
score_ypos = 1
score_font = pygame.font.Font("freesansbold.ttf",32)

for traffic_id in range(total_traffic):
    traffic_image.append(pygame.image.load("img/traffic_car_64_64.png"))
    traffic_xpos.append(random.randint(220,510))
    traffic_ypos.append(random.randint(-600, 5))
    traffic_ymove.append(5)

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
    score_value = score_font.render("Score : "+str(score),True,(255,255,255))
    screen.blit(score_value,(xvalue,yvalue))

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

        set_traffic(traffic_image[traffic_id],traffic_xpos[traffic_id],traffic_ypos[traffic_id])

    ## Setting Score ----------
    set_score(score_xpos, score_ypos)

    pygame.display.update()
