from img_load import load_image
import pygame


class Background(pygame.sprite.Sprite):
    image = load_image('background.png')

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Background.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass
