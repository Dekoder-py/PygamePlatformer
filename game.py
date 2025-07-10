import sys

import pygame

from scripts.entities import PhysicsEntity


class Game:
    def __init__(self):
        # initial setup
        pygame.init()

        pygame.display.set_caption("Unnamed Platformer")
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.test_entity = PhysicsEntity(self, "test", (300, 200), self.all_sprites)

    def run(self):
        while True:
            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill("#0fbfac")
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)

            # update the display and cap frame rate
            pygame.display.update()
            self.clock.tick(60)


Game().run()
