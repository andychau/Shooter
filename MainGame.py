import pygame
import time
import random
from TileClass import Tile
from PlayerClass import Player

pygame.init()

clock = pygame.time.Clock()

display_width = 900
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))

run1 = pygame.image.load('FinalRunning1.png')
run2 = pygame.image.load('FinalRunning2.png')
run3 = pygame.image.load('FinalRunning3.png')
run4 = pygame.image.load('FinalRunning4.png')
run5 = pygame.image.load('FinalRunning5.png')
run6 = pygame.image.load('FinalRunning6.png')
run7 = pygame.image.load('FinalRunning7.png')
run8 = pygame.image.load('FinalRunning8.png')
run9 = pygame.image.load('FinalRunning9.png')
run10 = pygame.image.load('FinalRunning10.png')
jump = pygame.image.load('FinalJumping.png')
fall = pygame.image.load('FinalFalling.png')

player1 = Player((90, 525), [run1, run2, run3, run4, run5, run6, run7, run8, run9, run10], jump, fall)


ground = pygame.image.load('GroundTile.png')
rightwall = pygame.image.load('RightWallTile.png')
leftwall = pygame.image.load('LeftWallTile.png')
groundTile = Tile(ground)
rightWallTile = Tile(rightwall)
leftWallTile = Tile(leftwall)

def draw_map():
	gameDisplay.fill((255, 255, 255)) #White
	groundTile.hplace12(30, 570) #Floor
	groundTile.hplace12(510, 570)
	groundTile.hplace12(30, 0) #Ceiling
	groundTile.hplace12(510, 0)
	leftWallTile.vplace6(0, 420) #Boundary
	rightWallTile.vplace6(870, 420)
	leftWallTile.vplace4(0, 0)
	rightWallTile.vplace4(870, 0)
	leftWallTile.vplace3(270, 480) #Left ground wall
	rightWallTile.vplace3(600, 480) #Right ground wall
	groundTile.hplace4(30, 420) #Lower left platform
	leftWallTile.vplace2(150, 390)
	groundTile.hplace4(750, 420) #Lower right platform
	rightWallTile.vplace2(720, 390)
	groundTile.hplace6(360, 390) #Lower center platform
	rightWallTile.vplace2(240, 270) #Left square block
	leftWallTile.vplace2(270, 270)
	rightWallTile.vplace2(600, 270) #Right square block
	leftWallTile.vplace2(630, 270)
	groundTile.hplace4(0, 240) #Upper left platform
	leftWallTile.vplace2(120, 210)
	leftWallTile.hplace1(0, 270)
	groundTile.hplace4(780, 240) #Upper right platform
	rightWallTile.vplace2(750, 210)
	rightWallTile.hplace1(870, 270)
	groundTile.hplace2(420, 90) #Pyramid
	groundTile.hplace4(390, 120)
	groundTile.hplace6(360, 150)

def player_action(player):
	player.xpos = player.xpos + player.xvel
	player.ypos = player.ypos + player.yvel
	player.place(player.xpos, player.ypos)

def player_yupdate(player):
	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_DOWN]:
		player.yvel = player.maxvel
		player.still = False
		player.falling = True
		player.jumping = False
	elif pressed[pygame.K_UP]:
		player.yvel = -player.maxvel
		player.still = False
		player.jumping = True
		player.falling = False
	else:
		player.yvel = 0
		player.jumping = False
		player.falling = False

def player_xupdate(player):
	pressed = pygame.key.get_pressed()

	if pressed[pygame.K_LEFT]:
		player.xvel = -player.maxvel
		player.still = False
		player.flip = True
	elif pressed[pygame.K_RIGHT]:
		player.xvel = player.maxvel
		player.still = False
		player.flip = False
	else:
		player.xvel = 0
		player.still = True

while True:
	draw_map()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
	player_xupdate(player1)
	player_yupdate(player1)
	player_action(player1)
	pygame.display.update()
	clock.tick(25)
