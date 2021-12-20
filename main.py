from img_load import load_image, screen
import pygame
from Background import Background
from Level import Level
from Player import Player
import time


def level(num):
    pygame.init()
    level_screen(num)
    running = True
    NEXTMOVE = pygame.USEREVENT + 1
    pygame.time.set_timer(NEXTMOVE, 4000)
    bg = pygame.sprite.Group()
    background = Background(bg)
    pl = pygame.sprite.Group()
    player = Player(pl)
    board = Level(9, 4, num)
    v_player = 120
    v_bullet = 300
    fps = 60
    time = pygame.time.Clock()
    bullets = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == NEXTMOVE:
                board.move()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append([player.rect.x + player.rect.w // 2 - 1, player.rect.y - 10])
        screen.fill((0, 0, 0))
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.rect.x > 0:
            player.rect.x -= v_player / fps
        if pygame.key.get_pressed()[pygame.K_RIGHT] and player.rect.x + player.rect.w < 450:
            player.rect.x += v_player / fps
        time.tick(fps)
        bg.draw(screen)
        pl.draw(screen)
        to_del = []
        for i in range(len(bullets)):
            bullets[i][1] -= v_bullet / fps
            pygame.draw.rect(screen, (255, 255, 255), (bullets[i][0], bullets[i][1], 2, 10))
            if board.get_click(bullets[i]):
                to_del.append(i)
            if bullets[i][1] < 0:
                to_del.append(i)
        for i in to_del:
            bullets.pop(i)
        if board.board == [[0] * 9 for _ in range(4)]:
            return 0
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


def level_screen(num):
    pygame.init()
    bg = pygame.sprite.Group()
    background = Background(bg)
    screen.fill((0, 0, 0))
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 50)
    text = font.render(f"LEVEL {num}", True, (255, 255, 255))
    text_x = background.rect.w // 2 - text.get_width() // 2
    text_y = background.rect.h // 2 - text.get_height() // 2
    bg.draw(screen)
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    time.sleep(1)


if __name__ == '__main__':
    running = True
    menu = pygame.sprite.Group()
    bg = Background(menu)
    play_button = pygame.sprite.Sprite(menu)
    play_button.image = load_image('play_button.png', colorkey=-1)
    play_button.rect = play_button.image.get_rect()
    play_button.rect.x = (bg.rect.w - play_button.rect.w) // 2
    play_button.rect.y = (bg.rect.h - play_button.rect.h) // 2
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_button.rect.collidepoint(event.pos):
                    for i in range(1, 14 + 1):
                        level(i)
                    running = False
        screen.fill((0, 0, 0))
        menu.draw(screen)
        pygame.display.flip()
    pygame.quit()
