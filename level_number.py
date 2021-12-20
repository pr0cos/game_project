import pygame


class Number(pygame.sprite.Sprite):
    def __init__(self, num, *groups):
        super().__init__(*groups)
        font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 30)
        self.image = font.render(f"LEVEL {num}", True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
