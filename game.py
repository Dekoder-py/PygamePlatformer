import sys

import pygame

# initial setup
pygame.init()

pygame.display.set_caption("Unnamed Platformer")
screen = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()

while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("#0fbfac")

    # update the display and cap frame rate
    pygame.display.update()
    clock.tick(60)
