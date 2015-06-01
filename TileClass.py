import pygame
pygame.init()
display_width = 900
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Tile:
	def __init__(self, image):
		self.image = image

	def hplace1(self, x, y):
		gameDisplay.blit(self.image, (x, y))

	def hplace2(self, x, y):
		self.hplace1(x, y)
		self.hplace1(x + 30, y)

	def hplace4(self, x, y):
		self.hplace2(x, y)
		self.hplace2(x + 60, y)

	def hplace6(self, x, y):
		self.hplace4(x, y)
		self.hplace2(x + 120, y)

	def hplace8(self, x, y):
		self.hplace4(x, y)
		self.hplace4(x + 120, y)

	def hplace12(self, x, y):
		self.hplace6(x, y)
		self.hplace6(x + 180, y)

	def vplace2(self, x, y):
		self.hplace1(x, y)
		self.hplace1(x, y + 30)

	def vplace3(self, x, y):
		self.vplace2(x, y)
		self.hplace1(x, y + 60)

	def vplace4(self, x, y):
		self.vplace2(x, y)
		self.vplace2(x, y + 60)

	def vplace6(self, x, y):
		self.vplace3(x, y)
		self.vplace3(x, y + 90)	