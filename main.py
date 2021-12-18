from img_load import screen
import pygame
from Background import Background
from Level import Level
from Player import Player


if __name__ == '__main__':
    running = True
    NEXTMOVE = pygame.USEREVENT + 1
    pygame.time.set_timer(NEXTMOVE, 6000)
    bg = pygame.sprite.Group()
    background = Background(bg)
    pl = pygame.sprite.Group()
    player = Player(pl)
    board = Level(9, 4, 4)
    v_player = 120
    v_bullet = 120
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
            if bullets[i][1] < 0:
                to_del.append(i)
        for i in to_del:
            bullets.pop(i)
        board.render(screen)
        pygame.display.flip()
    pygame.quit()
