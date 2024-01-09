import os, os.path
import sys
import pygame


need = False


def load_image(name, colorkey=None):
	fullname = os.path.join('data', name)
	# если файл не существует, то выходим
	if not os.path.isfile(fullname):
		print(f"Файл с изображением '{fullname}' не найден")
		sys.exit()
	image = pygame.image.load(fullname)
	if colorkey is not None:
		image = image.convert()
		if colorkey == -1:
			colorkey = image.get_at((0, 0))
		image.set_colorkey(colorkey)
	else:
		image = image.convert_alpha()
	return image


class Start:
	def __init__(self):
		self.width = 17
		self.height = 17
		self.cell_size = 30
		self.x, self.y, self.z = 5, 5, 5

	def get_cell(self, mouse_pos):
		x, y = mouse_pos
		if x in range(self.cell_size * self.width) and y in range(self.cell_size * self.height):
			return x // self.cell_size, y // self.cell_size
		return None

	def on_click(self, mouse_pos):
		cell = self.get_cell(mouse_pos)
		if cell:
			if cell[0] >= 0 and cell[1] >= 0:
				x, y = cell
				print(x, y)
				if x in range(4, 10) and y in range(7, 10):
					print(x, y)
					return True

	def render(self, surface):
		self.surface = surface
		for i in range(17):
			for j in range(17):
				pygame.draw.rect(self.surface, (10, 10, 10), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)
		for i in range(7, 10):
			for j in range(6, 11):
				pygame.draw.rect(self.surface, (250, 250, 250), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))



class Board:
	def __init__(self):
		self.width = 10
		self.height = 10
		self.length = 10
		self.lay = [[(60, 80, 30)] * 10 for _ in range(5)]
		self.lay += [[(60, 60, 30)] * 10 for _ in range(4)]
		self.lay += [[(225, 225, 225)] * 10]
		self.board = [self.lay for _ in range(self.width)]
		#self.board += [[[(60, 60, 30)] * self.width for _ in range(self.length)] for _ in range(self.height // 2 - 1)]
		#self.board += [[[(60, 80, 30)] * self.width for _ in range(self.length)]]
		self.cell_size = 30
		self.mosx, self.mosy = 25, 25
		self.x, self.y, self.z = 5, 5, 5
		self.left, self.top = 16, 3

	def render(self, surface):
		self.surface = surface
		for i in range(26):
			for j in range(51):
				pygame.draw.rect(self.surface, (10, 10, 10), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)
		self.cadr((self.mosx, self.mosy), self.surface)

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

	def cadr(self, coords, surface):
		self.mosx, self.mosy = coords[0] // self.cell_size, coords[1] // self.cell_size
		self.surface = surface
		for i in range(self.height * 2):
			for j in range(self.width * 2):
				pygame.draw.rect(self.surface, self.board[self.z][self.x][self.y], (self.left * self.cell_size + j * self.cell_size, self.cell_size * self.top + i * self.cell_size, self.cell_size, self.cell_size), 3)


pygame.init()
pygame.display.set_caption('Добро пожаловать! :)')
size = width, height = 510, 510
screen = pygame.display.set_mode(size)
start = Start()
running = True
pygame.mouse.set_visible(False)
all_sprites = pygame.sprite.Group()
sprite = pygame.sprite.Sprite()
sprite.image = load_image("arrow.png", colorkey=-1)
sprite.rect = sprite.image.get_rect()
all_sprites.add(sprite)
sprite.rect.x = 100
sprite.rect.y = 100
while running:
	screen.fill((0, 0, 0))
	start.render(screen)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			print(start.on_click(event.pos))
			if start.on_click(event.pos) == True:
				running = False
				need = True
		if event.type == pygame.MOUSEBUTTONUP:
			if start.on_click(event.pos) == True:
				pass
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEMOTION:
			if pygame.mouse.get_focused():
				x, y = event.pos
				sprite.rect.x = x
				sprite.rect.y = y
				all_sprites.draw(screen)
				pygame.display.flip()
pygame.quit()


if need:
        pygame.init()
        pygame.display.set_caption('Проектная игра')
        size = width, height = 1530, 780
        screen = pygame.display.set_mode(size)
        board = Board()
        running = True
        pygame.mouse.set_visible(False)
        all_sprites = pygame.sprite.Group()
        sprite = pygame.sprite.Sprite()
        sprite.image = load_image("arrow.png", colorkey=-1)
        sprite.rect = sprite.image.get_rect()
        all_sprites.add(sprite)
        sprite.rect.x = 100
        sprite.rect.y = 100
        heroes = pygame.sprite.Group()
        hero = pygame.sprite.Sprite()
        hero.image = load_image("hero.png", colorkey=-1)
        hero.rect = sprite.image.get_rect()
        heroes.add(hero)
        hero.rect.x = 300
        hero.rect.y = 300
        while running:
                screen.fill((0, 0, 0))
                board.render(screen)
                for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                x, y = event.pos
                        if event.type == pygame.QUIT:
                                running = False
                        if event.type == pygame.MOUSEMOTION:
                                board.cadr(event.pos, screen)
                                if pygame.mouse.get_focused():
                                        x, y = event.pos
                                        sprite.rect.x = x
                                        sprite.rect.y = y
                                        all_sprites.draw(screen)
                                        heroes.draw(screen)
                                        pygame.display.flip()
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
        pygame.quit()
