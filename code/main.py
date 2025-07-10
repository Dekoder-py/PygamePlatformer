import pygame

from player import Player


class Game:
    def __init__(self):
        # initial setup
        pygame.init()
        pygame.display.set_caption("Untitled Platformer")
        self.display_surface = pygame.display.set_mode((1280, 800))
        self.clock = pygame.Clock()
        self.running = True

        # sprites
        self.all_sprites = pygame.sprite.Group()
        self.player = Player(self.all_sprites)

    def run(self):
        while self.running:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill('skyblue')
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()

        pygame.quit()


game = Game()
game.run()
