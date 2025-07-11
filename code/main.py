from os.path import join

from pytmx.util_pygame import load_pygame

from level import Level
from settings import *


class Game:
    def __init__(self):
        pygame.init()
        self.display_surf = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Unnamed Platform World")
        self.clock = pygame.Clock()

        self.tmx_maps = {0: load_pygame(join("data", "levels", "omni.tmx"))}

        self.current_stage = Level(self.tmx_maps[0])

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.current_stage.run(dt)

            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
