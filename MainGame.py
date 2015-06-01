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

run1 = pygame.image.load('Running1.png')
run2 = pygame.image.load('Running2.png')
run3 = pygame.image.load('Running3.png')
run4 = pygame.image.load('Running4.png')
run5 = pygame.image.load('Running5.png')
run6 = pygame.image.load('Running6.png')
run7 = pygame.image.load('Running7.png')
run8 = pygame.image.load('Running8.png')
run9 = pygame.image.load('Running9.png')
run10 = pygame.image.load('Running10.png')
jump = pygame.image.load('Jumping.png')
fall = pygame.image.load('Falling.png')

player1 = Player([run1, run2, run3, run4, run5, run6, run7, run8, run9, run10], jump, fall)


ground = pygame.image.load('GroundTile.png')
rightwall = pygame.image.load('RightWallTile.png')
leftwall = pygame.image.load('LeftWallTile.png')
groundTile = Tile(ground)
rightWallTile = Tile(rightwall)
leftWallTile = Tile(leftwall)

def draw_map():
	gameDisplay.fill((255, 255, 255)) #Dark gray (40, 40, 40)
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

xpos, ypos = 90, 525

def player_action():
	global xpos
	global ypos
	xpos = xpos + player1.xvel
	ypos = ypos + player1.yvel
	player1.place(xpos, ypos)

while True:
	draw_map()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_a:
				player1.xvel = -player1.maxvel
				player1.flip = True
			elif event.key == pygame.K_d:
				player1.xvel = player1.maxvel
				player1.flip = False
			elif event.key == pygame.K_w:
				player1.yvel = -player1.maxvel
				player1.jumping = True
			elif event.key == pygame.K_s:
				player1.yvel = player1.maxvel
				player1.falling = True
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_a or event.key == pygame.K_d:
				player1.xvel = 0
			elif event.key == pygame.K_w:
				player1.yvel = 0
				player1.jumping = False
			elif event.key == pygame.K_s:
				player1.yvel = 0
				player1.falling = False

	player_action()
	pygame.display.update()
	clock.tick(25)
