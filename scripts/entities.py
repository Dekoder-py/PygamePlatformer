import pygame


class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, game, e_type, pos, size, *groups):
        super().__init__(*groups)
        self.game = game
        self.type = e_type
        self.pos = pygame.math.Vector2(pos)
        self.size = size
        self.velocity = [0, 0]

    def update(self, movement=(0, 0)):
        frame_movement = pygame.math.Vector2(
            movement[0] + self.velocity[0],
            movement[1] + self.velocity[1],
        )

        self.pos += frame_movement
        print(frame_movement)
