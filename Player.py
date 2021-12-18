import pygame
from img_load import load_image


class Player(pygame.sprite.Sprite):
    image = load_image('player.png', -1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = 190
        self.rect.y = 625

    def update(self, *args):
        if args and args[0].type == pygame.KEYDOWN:
            if args[0].key == pygame.K_RIGHT:
                self.rect.x += 10
            elif args[0].key == pygame.K_LEFT:
                self.rect.x -= 10
