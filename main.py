from img_load import load_image, screen
import pygame
from Background import Background
from Level import Level
from Player import Player
import time


def main():
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


def level(num):
    pygame.init()
    level_screen(num)
    running = True
    NEXTMOVE = pygame.USEREVENT + 1
    ALIEN1_ATTACK = pygame.USEREVENT + 2
    ALIEN2_ATTACK = pygame.USEREVENT + 3
    ALIEN3_ATTACK = pygame.USEREVENT + 4
    ALIEN4_ATTACK = pygame.USEREVENT + 5
    ALIEN5_ATTACK = pygame.USEREVENT + 6
    ALIEN6_ATTACK = pygame.USEREVENT + 7
    ALIEN7_ATTACK = pygame.USEREVENT + 8
    ALIEN8_ATTACK = pygame.USEREVENT + 9
    pygame.time.set_timer(NEXTMOVE, 4000)
    pygame.time.set_timer(ALIEN1_ATTACK, 2000)
    pygame.time.set_timer(ALIEN2_ATTACK, 3000)
    pygame.time.set_timer(ALIEN3_ATTACK, 4000)
    pygame.time.set_timer(ALIEN4_ATTACK, 3500)
    pygame.time.set_timer(ALIEN5_ATTACK, 2500)
    pygame.time.set_timer(ALIEN6_ATTACK, 3500)
    pygame.time.set_timer(ALIEN7_ATTACK, 4000)
    pygame.time.set_timer(ALIEN8_ATTACK, 2750)
    bg = pygame.sprite.Group()
    background = Background(bg)
    pl = pygame.sprite.Group()
    player = Player(pl)
    board = Level(9, 4, num)
    v_player = 300
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
            if event.type == ALIEN1_ATTACK:
                board.attack(1)
            if event.type == ALIEN2_ATTACK:
                board.attack(2)
            if event.type == ALIEN3_ATTACK:
                board.attack(3)
            if event.type == ALIEN4_ATTACK:
                board.attack(4)
            if event.type == ALIEN5_ATTACK:
                board.attack(5)
            if event.type == ALIEN6_ATTACK:
                board.attack(6)
            if event.type == ALIEN7_ATTACK:
                board.attack(7)
            if event.type == ALIEN8_ATTACK:
                board.attack(8)
        screen.fill((0, 0, 0))
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.rect.x > 0:
            player.rect.x -= v_player / fps
        if pygame.key.get_pressed()[pygame.K_RIGHT] and player.rect.x + player.rect.w < 450:
            player.rect.x += v_player / fps
        time.tick(fps)
        bg.draw(screen)
        pl.draw(screen)
        to_del = []
        for bullet in bullets:
            bullet[1] -= v_bullet / fps
            pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], 2, 10))
            if board.get_click(bullet):
                bullets.pop(bullets.index(bullet))
            if bullet[1] < 0:
                bullets.pop(bullets.index(bullet))
        for i in to_del:
            bullets.pop(i)
        for bullet in board.bullets:
            bullet[0][1] += v_bullet / fps
            pygame.draw.rect(screen, bullet[1], (bullet[0][0], bullet[0][1], 2, 10))
            if player.rect.collidepoint(bullet[0]):
                game_over()
            if bullet[0][1] > 700:
                board.bullets.pop(board.bullets.index(bullet))
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


def game_over():
    pygame.init()
    menu = pygame.sprite.Group()
    background = Background(menu)
    retry_button = pygame.sprite.Sprite(menu)
    retry_button.image = load_image('retry_button.png', colorkey=-1)
    retry_button.rect = retry_button.image.get_rect()
    retry_button.rect.x = (background.rect.w - retry_button.rect.w) // 2
    retry_button.rect.y = (background.rect.h - retry_button.rect.h) // 2
    screen.fill((0, 0, 0))
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 50)
    text = font.render("GAME OVER", True, (255, 255, 255))
    text_x = background.rect.w // 2 - text.get_width() // 2
    text_y = 100
    menu.draw(screen)
    screen.blit(text, (text_x, text_y))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and retry_button.rect.collidepoint(event.pos):
                    main()
                    running = False
                    pygame.quit()


if __name__ == '__main__':
    main()
