import pygame


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
		self.cell_size = 15
		self.mosx, self.mosy = 25, 25
		self.x, self.y, self.z = 5, 5, 5
		self.left, self.top = 31, 6

	def render(self, surface):
		self.surface = surface
		for i in range(self.height * 50):
			for j in range(self.width * 50):
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
		for i in range(self.height * 4):
			for j in range(self.width * 4):
				pygame.draw.rect(self.surface, self.board[self.z][self.x][self.y], (self.left * self.cell_size + j * self.cell_size, self.cell_size * self.top + i * self.cell_size, self.cell_size, self.cell_size), 5)


pygame.init()
pygame.display.set_caption('Инициализация игры')
size = width, height = 1530, 780
screen = pygame.display.set_mode(size)
board = Board()
running = True
while running:
	board.render(screen)
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			x, y = event.pos
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEMOTION:
			board.cadr(event.pos, screen)
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
