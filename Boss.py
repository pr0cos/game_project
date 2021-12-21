from img_load import load_image
import pygame


class Boss(pygame.sprite.Sprite):
    image = load_image('boss.png', -1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Boss.image
        self.rect = self.image.get_rect()
        self.rect.x = 129
        self.rect.y = 100
        self.hp = 50
        self.side = 1
        self.bullets = []
        self.circles = []
        self.lasers = []


class Circle(pygame.sprite.Sprite):
    image = load_image('circle.png', -1)

    def __init__(self, x, y, v_x, v_y, *groups):
        super().__init__(*groups)
        self.image = Circle.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.mask = pygame.mask.from_surface(self.image)


class Laser(pygame.sprite.Sprite):
    image = load_image('laser.png')

    def __init__(self, x, *groups):
        super().__init__(*groups)
        self.image = Laser.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = 0
