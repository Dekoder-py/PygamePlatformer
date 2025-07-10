import sys

import pygame


class Game:
    def __init__(self):
        # initial setup
        pygame.init()

        pygame.display.set_caption("Unnamed Platformer")
        self.screen = pygame.display.set_mode((640, 480))

        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("#0fbfac")

            # update the display and cap frame rate
            pygame.display.update()
            self.clock.tick(60)


Game().run()
