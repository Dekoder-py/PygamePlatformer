from os.path import join

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('assets', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(300, 300))
