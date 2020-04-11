import pygame
pygame.init()
#create the screen
screen=pygame.display.set_mode((800,600))


pygame.display.set_caption("Space Invaders")
iconrocket = pygame.image.load('rocket.png')
pygame.display.set_icon(iconrocket)

spaceship = pygame.image.load('spaceship.png')
spaceshipX=370
spaceshipY=480
spaceshipX_change=0


def arcadespaceship(x,y):
    screen.blit(spaceship,(x,y))






#game loop
running=True
while running:
    # rgb
    screen.fill((0, 0, 0))
    spaceshipX+=0.3
    print(spaceshipX)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        if event.type
    arcadespaceship(spaceshipX,spaceshipY)
    pygame.display.update()