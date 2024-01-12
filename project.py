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
		self.sprite_group = pygame.sprite.Group()
		self.sprite = pygame.sprite.Sprite()
		self.sprite.image = load_image("nether.png")
		self.sprite.rect = self.sprite.image.get_rect()
		self.sprite_group.add(self.sprite)
		self.sprite.rect.x = 0
		self.sprite.rect.y = 0

	def draw(self, screen):
		font = pygame.font.Font(None, 100)
		text = font.render("A hot walk", True, (10, 10, 10))
		text_x = 10
		text_y = 10
		text_w = text.get_width()
		text_h = text.get_height()
		screen.blit(text, (text_x, text_y))
		pygame.draw.rect(screen, (0, 255, 0), (text_x - 10, text_y - 10, text_w + 20, text_h + 20), 1)


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
				if x in range(4, 10) and y in range(7, 10):
					return True

	def render(self, surface, other):
		self.surface = surface
		for i in range(17):
			for j in range(17):
				pygame.draw.rect(self.surface, (10, 10, 10), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)
		self.sprite_group.draw(self.surface)
		for i in range(7, 10):
			for j in range(6, 11):
				pygame.draw.rect(self.surface, (100, 10, 10), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))
		
		if other:
			for i in range(7, 10):
				for j in range(6, 11):
					pygame.draw.rect(self.surface, (100, 50, 50), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size))


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
		self.cell_size = 50
		self.mosx, self.mosy = 25, 25
		self.x, self.y, self.z = 5, 5, 5
		self.left, self.top = 9, 1

	def render(self, surface, krug):
		self.surface = surface
		self.krug = krug
		for i in range(16):
			for j in range(31):
				pygame.draw.rect(self.surface, (10, 10, 10), (j * self.cell_size, i * self.cell_size, self.cell_size, self.cell_size), 1)
		self.cadr((self.mosx, self.mosy), self.surface)

	def get_cell(self, mouse_pos):
		x, y = mouse_pos
		if x in range(self.cell_size * self.left + krug * self.cell_size, self.cell_size * self.left + krug * self.cell_size + (13 - krug) * self.cell_size) and y in range(self.cell_size * self.top + krug * self.cell_size, self.cell_size * self.top + krug * self.cell_size + (13 - krug) * self.cell_size):
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
		pygame.draw.rect(self.surface, (100, 20, 20), ((9 + krug) * self.cell_size, (1 + krug) * self.cell_size, (13 - krug) * self.cell_size, (13 - krug) * self.cell_size))
		for i in range(krug, 13 - self.krug):
			for j in range(krug, 13 - self.krug):
				pygame.draw.rect(self.surface, self.board[self.z][self.x][self.y], (self.left * self.cell_size + j * self.cell_size, self.cell_size * self.top + i * self.cell_size, self.cell_size, self.cell_size), 1)
		pygame.draw.rect(self.surface, self.board[self.z][self.x][self.y], (self.left * self.cell_size + krug * self.cell_size, self.cell_size * self.top + krug * self.cell_size, self.cell_size * (13 - krug), self.cell_size * (13 - krug)), 2)


change = False
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
skulls = pygame.sprite.Group()
skull = pygame.sprite.Sprite()
skull.image = load_image("skull.png", colorkey=-1)
skull.rect = skull.image.get_rect()
skulls.add(skull)
skull.rect.x = 210
skull.rect.y = 210
while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		match event.type:
			case pygame.MOUSEBUTTONUP:
				if start.on_click(event.pos):
					need = True
					change = False
					running = False
				else:
					change = False
					start.render(screen, change)
					start.draw(screen)
					skulls.draw(screen)
					all_sprites.draw(screen)
					pygame.display.flip()
			case pygame.MOUSEBUTTONDOWN:
				if start.on_click(event.pos):
					change = True
					x, y = event.pos
					sprite.rect.x = x
					sprite.rect.y = y
					start.render(screen, change)
					start.draw(screen)
					skulls.draw(screen)
					all_sprites.draw(screen)
					pygame.display.flip()
			case pygame.QUIT:
				running = False
			case pygame.MOUSEMOTION:
				if pygame.mouse.get_focused():
					x, y = event.pos
					sprite.rect.x = x
					sprite.rect.y = y
					start.render(screen, change)
					start.draw(screen)
					skulls.draw(screen)
					all_sprites.draw(screen)
					pygame.display.flip()
pygame.quit()


if need:
	krug = 0
	pygame.init()
	pygame.display.set_caption('Проектная игра')
	size = width, height = 1550, 800
	screen = pygame.display.set_mode(size)
	board = Board()
	running = True
	pygame.mouse.set_visible(False)
	heroes = pygame.sprite.Group()
	hero = pygame.sprite.Sprite()
	hero.image = load_image("hero.png", colorkey=-1)
	hero.rect = sprite.image.get_rect()
	heroes.add(hero)
	herx = 10 * 50 + krug * 50
	hery = 2 * 50 + krug * 50
	hero.rect.x = herx
	hero.rect.y = hery
	moving = False
	while running:
		screen.fill((0, 0, 0))
		board.render(screen, krug)
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				x, y = event.pos
				if (x in range(hero.rect.x - 35, hero.rect.x + 35) and y in range(hero.rect.y - 35, hero.rect.y + 35)):
					moving = True
					nachx, nachy = event.pos
			if event.type == pygame.QUIT:
				running = False
			if event.type == pygame.MOUSEMOTION:
				if pygame.mouse.get_focused():
					x, y = event.pos
					sprite.rect.x = x
					sprite.rect.y = y
					heroes.draw(screen)
					all_sprites.draw(screen)
					pygame.display.flip()
					if moving:
						xrel, yrel = event.rel
						hero.rect.x += xrel
						hero.rect.y += yrel
				board.cadr(event.pos, screen)
			if event.type == pygame.MOUSEBUTTONUP:
				if moving:
					if x + 20 not in range(450 + krug * 50, 450 + krug * 50 + (13 - krug) * 50) or y + 20 not in range(50 + krug * 50, 450 + krug * 50 + (13 - krug) * 50):
						hero.rect.x = nachx
						hero.rect.y = nachy
					moving = False
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
			if event.type == pygame.K_RETURN:
				pass
	pygame.quit()
