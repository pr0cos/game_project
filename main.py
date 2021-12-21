from img_load import load_image, screen, width, height
import pygame
from Background import Background
from Level import Level
from Player import Player
import time
from level_number import Number
from Boss import Boss, Circle, Laser
import random


def main():
    running = True
    menu = pygame.sprite.Group()
    bg = Background(menu)
    play_button = pygame.sprite.Sprite(menu)
    play_button.image = load_image('play_button.png', colorkey=-1)
    play_button.rect = play_button.image.get_rect()
    play_button.rect.x = (bg.rect.w - play_button.rect.w) // 2
    play_button.rect.y = (bg.rect.h - play_button.rect.h) // 2
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 100)
    text1 = pygame.sprite.Sprite(menu)
    text1.image = font.render("SPACE", True, (255, 255, 255))
    text1.rect = text1.image.get_rect()
    text1.rect.x = bg.rect.w // 2 - text1.rect.w // 2
    text1.rect.y = 50
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 50)
    text2 = pygame.sprite.Sprite(menu)
    text2.image = font.render("INVESTORS", True, (255, 255, 255))
    text2.rect = text2.image.get_rect()
    text2.rect.x = bg.rect.w // 2 - text2.rect.w // 2
    text2.rect.y = 150
    menu.draw(screen)
    pygame.display.flip()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_button.rect.collidepoint(event.pos):
                    for i in range(1, 14 + 1):
                        level(i)
                    boss_fight()
                    running = False
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
    level = Number(num, bg)
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
        if pygame.key.get_pressed()[pygame.K_RIGHT] and player.rect.x + player.rect.w < width:
            player.rect.x += v_player / fps
        time.tick(fps)
        bg.draw(screen)
        pl.draw(screen)
        for bullet in bullets:
            bullet[1] -= v_bullet / fps
            pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], 2, 10))
            if board.get_click(bullet):
                bullets.pop(bullets.index(bullet))
            if bullet[1] < 0:
                bullets.pop(bullets.index(bullet))
        for bullet in board.bullets:
            bullet[0][1] += v_bullet / fps
            pygame.draw.rect(screen, bullet[1], (bullet[0][0], bullet[0][1], 2, 10))
            if player.rect.collidepoint(bullet[0]):
                game_over()
            if bullet[0][1] > height:
                board.bullets.pop(board.bullets.index(bullet))
        if board.board == [[0] * 9 for _ in range(4)]:
            return 0
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


def boss_fight():
    pygame.init()
    level_screen(-1)
    running = True
    rage = False
    rage_started = False
    laser_attack_started = False
    laser_hide_started = False
    BULLET_ATTACK = pygame.USEREVENT + 1
    CIRCLE_ATTACK = pygame.USEREVENT + 2
    RAGE_ATTACK = pygame.USEREVENT + 3
    END_RAGE = pygame.USEREVENT + 4
    START_RAGE_FUNCTION = pygame.USEREVENT + 5
    LASER_ATTACK = pygame.USEREVENT + 6
    LASER_SHOW = pygame.USEREVENT + 7
    LASER_HIDE = pygame.USEREVENT + 8
    START_LASER_ATTACK = pygame.USEREVENT + 9
    START_LASER_HIDE = pygame.USEREVENT + 10
    pygame.time.set_timer(BULLET_ATTACK, 3000)
    pygame.time.set_timer(CIRCLE_ATTACK, 7000)
    pygame.time.set_timer(START_RAGE_FUNCTION, 3000)
    pygame.time.set_timer(RAGE_ATTACK, 8000)
    pygame.time.set_timer(LASER_SHOW, 10000)
    pygame.time.set_timer(START_LASER_ATTACK, 4000)
    pygame.time.set_timer(START_LASER_HIDE, 6000)
    bg = pygame.sprite.Group()
    pl = pygame.sprite.Group()
    boss = pygame.sprite.Group()
    circles = pygame.sprite.Group()
    lasers = pygame.sprite.Group()
    background = Background(bg)
    bs = Boss(boss)
    player = Player(pl)
    v_player = 300
    v_bullet = 300
    v_boss = 100
    v_rage_boss = 300
    fps = 60
    time = pygame.time.Clock()
    bullets = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append([player.rect.x + player.rect.w // 2 - 1, player.rect.y - 10])
            if event.type == BULLET_ATTACK:
                bs.bullets.append([bs.rect.x + 41, bs.rect.y + bs.rect.h])
                bs.bullets.append([bs.rect.x + 95, bs.rect.y + bs.rect.h])
                bs.bullets.append([bs.rect.x + 149, bs.rect.y + bs.rect.h])
            if event.type == CIRCLE_ATTACK:
                rect_x = bs.rect.x + bs.rect.w // 2 - bs.rect.w // 2
                rect_y = bs.rect.y + bs.rect.h // 2 - bs.rect.h // 2
                for x in range(0, 100 + 1, 25):
                    y = round((10000 - x ** 2) ** (1 / 2))
                    bs.circles.append([rect_x, rect_y, -x, -y])
                    bs.circles.append([rect_x, rect_y, x, -y])
                    bs.circles.append([rect_x, rect_y, -x, y])
                    bs.circles.append([rect_x, rect_y, x, y])
            if event.type == START_RAGE_FUNCTION and not rage_started:
                rage_started = True
                pygame.time.set_timer(END_RAGE, 8000)
                pygame.time.set_timer(START_RAGE_FUNCTION, 0)
            if event.type == RAGE_ATTACK:
                rage = True
                pygame.time.set_timer(BULLET_ATTACK, 750)
            if event.type == END_RAGE:
                rage = False
                pygame.time.set_timer(BULLET_ATTACK, 3000)
            if event.type == START_LASER_ATTACK and not laser_attack_started:
                laser_attack_started = True
                pygame.time.set_timer(LASER_ATTACK, 10000)
                pygame.time.set_timer(START_LASER_ATTACK, 0)
            if event.type == START_LASER_HIDE and not laser_hide_started:
                laser_hide_started = True
                pygame.time.set_timer(LASER_HIDE, 10000)
                pygame.time.set_timer(START_LASER_HIDE, 0)
            if event.type == LASER_SHOW:
                probably_nums = range(width - 25 + 1)
                used = []
                for _ in range(3):
                    while True:
                        i = random.choice(probably_nums)
                        if i not in used:
                            break
                    for j in range(i - 25, i + 26):
                        used.append(j)
                    bs.lasers.append([i, False])
            if event.type == LASER_ATTACK:
                for laser in bs.lasers:
                    laser[1] = True
            if event.type == LASER_HIDE:
                bs.lasers.clear()
        screen.fill((0, 0, 0))
        bg.draw(screen)
        pygame.draw.rect(screen, (255, 255, 255), ((width - 204) // 2, 10, 204, 40), 2)
        pygame.draw.rect(screen, (255, 0, 0), ((width - 204) // 2 + 2, 12, bs.hp * 4, 36))
        if pygame.key.get_pressed()[pygame.K_LEFT] and player.rect.x > 0:
            player.rect.x -= v_player / fps
        if pygame.key.get_pressed()[pygame.K_RIGHT] and player.rect.x + player.rect.w < width:
            player.rect.x += v_player / fps
        pl.draw(screen)
        if not rage:
            bs.rect.x += (v_boss / fps) * bs.side
        else:
            bs.rect.x += (v_rage_boss / fps) * bs.side
        if bs.rect.x <= 0 or bs.rect.x + bs.rect.w >= width:
            bs.side *= -1
        boss.draw(screen)
        for bullet in bullets:
            bullet[1] -= v_bullet / fps
            pygame.draw.rect(screen, (255, 255, 255), (bullet[0], bullet[1], 2, 10))
            if bs.rect.collidepoint(bullet):
                bs.hp -= 1
                bullets.pop(bullets.index(bullet))
            if bullet[1] < 0:
                bullets.pop(bullets.index(bullet))
        for bullet in bs.bullets:
            bullet[1] += v_bullet / fps
            pygame.draw.rect(screen, (255, 0, 0), (bullet[0], bullet[1], 2, 10))
            if player.rect.collidepoint(bullet):
                game_over()
            if bullet[1] > height:
                bs.bullets.pop(bs.bullets.index(bullet))
        for circle in bs.circles:
            c = Circle(*circle, circles)
            if pygame.sprite.collide_mask(c, player):
                game_over()
            if c.rect.x + c.rect.w < 0 or c.rect.x > width:
                if circle in bs.circles:
                    bs.circles.pop(bs.circles.index(circle))
            if c.rect.y + c.rect.h < 0 or c.rect.y > height:
                if circle in bs.circles:
                    bs.circles.pop(bs.circles.index(circle))
            circle[0] += circle[2] / fps
            circle[1] += circle[3] / fps
        circles.draw(screen)
        circles.empty()
        for laser in bs.lasers:
            if laser[1]:
                las = Laser(laser[0], lasers)
                if pygame.sprite.spritecollideany(las, pl):
                    game_over()
            else:
                pygame.draw.rect(screen, (255, 255, 255), (laser[0] + 11, 0, 3, height))
        lasers.draw(screen)
        lasers.empty()
        if bs.hp <= 0:
            congratulation()
        time.tick(fps)
        pygame.display.flip()
    pygame.quit()


def level_screen(num):
    pygame.init()
    bg = pygame.sprite.Group()
    background = Background(bg)
    screen.fill((0, 0, 0))
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 50)
    if num == -1:
        text = font.render(f"BOSS FIGHT", True, (255, 255, 255))
        text_x = background.rect.w // 2 - text.get_width() // 2
        text_y = background.rect.h // 2 - text.get_height() // 2
        bg.draw(screen)
        screen.blit(text, (text_x, text_y))
        pygame.display.flip()
        time.sleep(1)
        return None
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and retry_button.rect.collidepoint(event.pos):
                    main()
    pygame.quit()


def congratulation():
    pygame.init()
    menu = pygame.sprite.Group()
    background = Background(menu)
    play_again_button = pygame.sprite.Sprite(menu)
    play_again_button.image = load_image('play_again_button.png', colorkey=-1)
    play_again_button.rect = play_again_button.image.get_rect()
    play_again_button.rect.x = (background.rect.w - play_again_button.rect.w) // 2
    play_again_button.rect.y = (background.rect.h - play_again_button.rect.h) // 2
    screen.fill((0, 0, 0))
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 35)
    text1 = pygame.sprite.Sprite(menu)
    text1.image = font.render("CONGRATULATIONS", True, (255, 255, 255))
    text1.rect = text1.image.get_rect()
    text1.rect.x = background.rect.w // 2 - text1.rect.w // 2
    text1.rect.y = 50
    font = pygame.font.Font('font/Kemco Pixel Bold.ttf', 30)
    text2 = pygame.sprite.Sprite(menu)
    text2.image = font.render("YOU PASSED THE GAME", True, (255, 255, 255))
    text2.rect = text2.image.get_rect()
    text2.rect.x = background.rect.w // 2 - text2.rect.w // 2
    text2.rect.y = 100
    menu.draw(screen)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and play_again_button.rect.collidepoint(event.pos):
                    main()
    pygame.quit()


if __name__ == '__main__':
    main()
