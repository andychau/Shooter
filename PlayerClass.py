import pygame
import time
pygame.init()
display_width = 900
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

class Player:

	def __init__(self, position, imglist, jumpsprite, fallsprite):
		self.xpos = position[0]
		self.ypos = position[1]
		self.imglist = imglist
		self.jumpsprite = jumpsprite
		self.fallsprite = fallsprite
		self.stillsprite = imglist[8]
		self.imgtrack = 0
		self.xvel = 0
		self.yvel = 0
		self.maxvel = 5
		self.flip = False
		self.jumping = False
		self.falling = False
		self.still = True

	def place(self, posx, posy):
		if not self.jumping and not self.falling and not self.still:
			if not self.flip:
				gameDisplay.blit(self.imglist[self.imgtrack], (posx, posy))
				self.imgtrack = (self.imgtrack + 1) % len(self.imglist)
			else:
				gameDisplay.blit(pygame.transform.flip(self.imglist[self.imgtrack], True, False), (posx, posy))
				self.imgtrack = (self.imgtrack + 1) % len(self.imglist)
		else:
			if self.still:
				if not self.flip:
					gameDisplay.blit(self.stillsprite, (posx, posy))
				else:
					gameDisplay.blit(pygame.transform.flip(self.stillsprite, True, False), (posx, posy))
			elif self.jumping:
				if not self.flip:
					gameDisplay.blit(self.jumpsprite, (posx, posy))
				else:
					gameDisplay.blit(pygame.transform.flip(self.jumpsprite, True, False), (posx, posy))
			elif self.falling:
				if not self.flip:
					gameDisplay.blit(self.fallsprite, (posx, posy))
				else:
					gameDisplay.blit(pygame.transform.flip(self.fallsprite, True, False), (posx, posy))