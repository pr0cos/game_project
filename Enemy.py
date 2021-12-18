from img_load import load_image
import pygame


class Alien1(pygame.sprite.Sprite):
    image = load_image('alien1.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien1.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien2(pygame.sprite.Sprite):
    image = load_image('alien2.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien2.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien3(pygame.sprite.Sprite):
    image = load_image('alien3.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien3.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien4(pygame.sprite.Sprite):
    image = load_image('alien4.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien4.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien5(pygame.sprite.Sprite):
    image = load_image('alien5.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien5.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien6(pygame.sprite.Sprite):
    image = load_image('alien6.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien6.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien7(pygame.sprite.Sprite):
    image = load_image('alien7.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien7.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass


class Alien8(pygame.sprite.Sprite):
    image = load_image('alien8.png', colorkey=-1)

    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = Alien8.image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, *args):
        pass
