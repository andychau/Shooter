import pygame
import time
pygame.init()
display_width = 900
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Player:

	def __init__(self, imglist, jumpsprite, fallsprite):
		self.imglist = imglist
		self.jumpsprite = jumpsprite
		self.fallsprite = fallsprite
		self.imgtrack = 0
		self.xvel = 0
		self.yvel = 0
		self.maxvel = 5
		self.flip = False
		self.jumping = False
		self.falling = False

	def place(self, posx, posy):
		if not self.jumping and not self.falling:
			if not self.flip:
				gameDisplay.blit(pygame.transform.scale(self.imglist[self.imgtrack], (30, 45)), (posx, posy))
				self.imgtrack = (self.imgtrack + 1) % len(self.imglist)
			else:
				gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(self.imglist[self.imgtrack], (30, 45)), True, False), (posx, posy))
				self.imgtrack = (self.imgtrack + 1) % len(self.imglist)
		else:
			if not self.falling:
				if not self.flip:
					gameDisplay.blit(pygame.transform.scale(self.jumpsprite, (30, 45)), (posx, posy))
				else:
					gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(self.jumpsprite, (30, 45)), True, False), (posx, posy))
			else:
				if not self.flip:
					gameDisplay.blit(pygame.transform.scale(self.fallsprite, (30, 45)), (posx, posy))
				else:
					gameDisplay.blit(pygame.transform.flip(pygame.transform.scale(self.fallsprite, (30, 45)), True, False), (posx, posy))