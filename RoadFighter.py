import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Road Fighter - [YYSCOOP.com]")
favicon = pygame.image.load("img/favicon.ico")
pygame.display.set_icon(favicon)


## Main Game Loop -------------------------
running = True
while running:
    screen.fill((255,40,80))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
