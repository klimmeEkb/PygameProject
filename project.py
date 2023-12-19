import pygame
import random


class Board:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.length = 10
        self.board = [[[(225, 225, 225)] * self.width for _ in range(self.length)]]
        self.board += [[[(60, 60, 30)] * self.width for _ in range(self.length)] for _ in range(self.height // 2 - 1)]
        self.board += [[[(60, 80, 30)] * self.width for _ in range(self.length)] for _ in range(self.height // 2)]
        self.sees = 6
        self.cell_size = 15
        self.x, self.y = 375, 375

    def set_view(self, cell_size):
        self.cell_size = cell_size

    def render(self, surface):
        self.surface = surface
        for i in range(self.height):
            for j in range(self.width):
                pygame.draw.rect(self.surface, self.board[self.sees][i][j][0], (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 7)

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        if x in range(self.cell_size * self.width) and y in range(self.cell_size * self.height):
            return x // self.cell_size, y // self.cell_size
        return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            if cell[0] >= 0 and cell[1] >= 0:
                self.on_click(cell)

    def cadr(self, coords):
        self.x, self.y = coords


pygame.init()
pygame.display.set_caption('Инициализация игры')
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
board = Board()
running = True
while running:
    board.render(screen)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            drawing = True
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            board.cadr(event.pos)
        if event.type == pygame.K_w:
            pass
        if event.type == pygame.K_a:
            pass
        if event.type == pygame.K_s:
            pass
        if event.type == pygame.K_d:
            pass
        if event.type == pygame.K_SPACE:
            pass
    board.render(screen)
    pygame.display.flip()
