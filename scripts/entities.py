from os.path import join

import pygame


class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, game, e_type, pos, *groups):
        super().__init__(*groups)
        self.game = game
        self.type = e_type
        self.velocity = pygame.math.Vector2(1, 0)
        self.image = pygame.image.load(
            join("data", "images", "entities", "player.png")
        ).convert()
        self.rect = self.image.get_frect(center=pos)
        self.image.set_colorkey("#000000")

    def update(self, movement=(0, 0)):
        frame_movement = pygame.math.Vector2(
            movement[0] + self.velocity[0],
            movement[1] + self.velocity[1],
        )

        self.rect.center += frame_movement
