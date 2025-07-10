from os.path import join

import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(join('assets', 'images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(300, 300))
        self.on_ground = True
        self.direction = pygame.math.Vector2()
        self.speed = 400

    def update(self, delta):
        keys = pygame.key.get_pressed()
        right_keys_pressed = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        left_keys_pressed = keys[pygame.K_a] or keys[pygame.K_LEFT]
        self.direction.x = int(right_keys_pressed) - int(left_keys_pressed)
        self.rect.center += self.direction * self.speed * delta
