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


def set_player(xvalue,yvalue):
    xvalue = int(xvalue)
    yvalue = int(yvalue)
    screen.blit(player_image, (xvalue, yvalue))


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

    ## Updating player possition
    player_xpos = player_xpos + player_xmove

    ## Creating boundaries for player
    if player_xpos <= 220:
        player_xpos = 220
    if player_xpos >= 510:
        player_xpos = 510


    ## Setting player New position
    set_player(player_xpos,player_ypos)


    pygame.display.update()

