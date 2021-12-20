from Board import Board
from Enemy import *
import random
import pygame


class Level(Board):

    def __init__(self, width, height, lvl_number):
        super().__init__(width, height)
        self.lvl_number = lvl_number
        self.enemies = pygame.sprite.Group()
        self.bullets = []
        for _ in range(self.lvl_number * 2):
            while True:
                x = random.randrange(0, self.height)
                y = random.randrange(0, self.width)
                if self.board[x][y] == 0:
                    break
            if self.board[x][y] == 0:
                n = random.randrange(1, 9)
                if n == 1:
                    self.board[x][y] = Alien1(self.enemies)
                if n == 2:
                    self.board[x][y] = Alien2(self.enemies)
                if n == 3:
                    self.board[x][y] = Alien3(self.enemies)
                if n == 4:
                    self.board[x][y] = Alien4(self.enemies)
                if n == 5:
                    self.board[x][y] = Alien5(self.enemies)
                if n == 6:
                    self.board[x][y] = Alien6(self.enemies)
                if n == 7:
                    self.board[x][y] = Alien7(self.enemies)
                if n == 8:
                    self.board[x][y] = Alien8(self.enemies)

    def render(self, screen):
        for x in range(self.height):
            for y in range(self.width):
                if self.board[x][y] != 0:
                    self.board[x][y].rect.x = self.left + self.cell_size * y
                    self.board[x][y].rect.y = self.top + self.cell_size * x
        self.enemies.draw(screen)

    def move(self):
        cells = ((-1, 0), (0, -1), (1, 0), (0, 1))
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] != 0 and not self.board[y][x].was_moved:
                    c = random.choices(cells, k=4)
                    flag = False
                    for cell in c:
                        try:
                            x0 = x + cell[0]
                            y0 = y + cell[1]
                            if x0 >= 0 and y >= 0:
                                if self.board[y0][x0] == 0:
                                    self.board[y0][x0], self.board[y][x] = self.board[y][x], self.board[y0][x0]
                                    self.board[y0][x0].was_moved = True
                                    flag = True
                        except IndexError:
                            pass
                        if flag:
                            break
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] != 0:
                    self.board[y][x].was_moved = False

    def on_click(self, cell):
        self.board[int(cell[1])][int(cell[0])].kill()
        self.board[int(cell[1])][int(cell[0])] = 0

    def attack(self, num):
        if num == 1:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien1:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 2:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien2:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 3:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien3:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 4:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien4:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 5:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien5:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 6:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien6:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 7:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien7:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
        if num == 8:
            for x in range(self.width):
                for y in range(self.height):
                    if type(self.board[y][x]) is Alien8:
                        self.bullets.append([[self.left + self.cell_size * (x + 0.5),
                                              self.top + self.cell_size * (y + 1)],
                                             self.board[y][x].bullet_color])
