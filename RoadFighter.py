import random
import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Road Fighter - [YYSCOOP.com]")
favicon = pygame.image.load("img/favicon.ico")
pygame.display.set_icon(favicon)

game_background = pygame.image.load("img/background_road_800_600.png")

## Player
player_image = pygame.image.load("img/player_car_68_127.png")
player_xpos = 280
player_ypos = 465
player_xmove = 0

#Traffic
traffic_image = []
traffic_xpos = []
traffic_ypos = []
# traffic_xmove = []
traffic_ymove = []
total_traffic = 2

for traffic_id in range(total_traffic):
    traffic_image.append(pygame.image.load("img/traffic_car.png"))
    traffic_xpos.append(random.randint(220,510))
    if traffic_id == 0:
        traffic_ypos.append(5)
    if traffic_id == 1:
        traffic_ypos.append(-255)
    # traffic_xmove = 0
    traffic_ymove.append(5)

def set_player(xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    screen.blit(player_image,(xvalue, yvalue))

def set_traffic(image,xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    screen.blit(image, (xvalue, yvalue))


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
    if player_xpos >= 510:
        player_xpos = 510
    ## Setting player New position
    set_player(player_xpos,player_ypos)

    ## Updating / creating / setting traffic positions

    for traffic_id in range(total_traffic):
        traffic_ypos[traffic_id] = traffic_ypos[traffic_id] + traffic_ymove[traffic_id]

        if traffic_ypos[0] >= 600:                      
            traffic_ypos[0] = 10
            traffic_xpos[traffic_id] = random.randint(220, 510)

            if traffic_ypos[1] >= 600:
                traffic_ypos[1] = -325
                traffic_xpos[traffic_id] = random.randint(220, 510)


        set_traffic(traffic_image[traffic_id],traffic_xpos[traffic_id],traffic_ypos[traffic_id])

    pygame.display.update()
