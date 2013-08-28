import pygame, sys
import math
from pygame.locals import *

class Player(object):
	def setPosition(self, xpos, ypos):
		self.x = xpos
		self.y = ypos
		self.rect = pygame.Rect(xpos - 10, ypos - 10, 20, 20)
		self.dx = 0.0
		self.dy = 0.0

	def setController(self, cont):
		self.controller = cont

	def setSpeed(self, dx, dy):
		self.dx = dx
		self.dy = dy

	def move(self):
		self.x += dx
		self.y += dy
		self.rect.move_ip(self.dx,self.dy)


pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
dispWidth = 400
dispHeight = 300
DISPLAYSURF = pygame.display.set_mode((dispWidth, dispHeight))
pygame.display.set_caption('Magneto')

# set up xbox controllers
joysticks = []
players = []
noOfPlayers = pygame.joystick.get_count()
print("Number of players: ", noOfPlayers)
for i in range(0, noOfPlayers):
	players.append(Player())
	players[-1].setController(pygame.joystick.Joystick(i))
	players[-1].controller.init()
	players[-1].setPosition(dispWidth/(noOfPlayers + 1) * (i + 1),dispHeight/2)
    #joysticks.append(pygame.joystick.Joystick(i))
    #joysticks[-1].init()
    #print("Detected joystick '",joysticks[-1].get_name(),"'")



# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0 , 0)
GREEN = (255, 255, 255)
BLUE = (0, 0, 255)
ActiveColor = BLUE

# draw on the surface object
'''
mainRect = pygame.Rect((200, 150, 20, 20))
aimRect = pygame.Rect((260, 160, 10, 10))
pygame.draw.rect(DISPLAYSURF, BLUE, mainRect)
'''

# set up movement
dx = 0.0
dy = 0.0
katetx = 50
katety = 0
katetx_raw = 1
katety_raw = 0

player = 0
# run the game loop
while True:
	DISPLAYSURF.fill(BLACK)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
		if event.type == JOYAXISMOTION:
			#print("Joystick '",joysticks[event.joy].get_name(),"' axis",event.axis,"motion.")
			print("Player ", event.joy)
			player = event.joy
			if event.axis == 0:
				# axis 0 is x-axis
				print(' axis 0', event.value)
				dx = 5 * event.value
			elif event.axis == 1:
				# axis 1 is y-axis
				print(' axis 1', event.value)
				dy = 5 * event.value
			elif event.axis == 2:
				# axis 1 is y-axis
				print(' axis 2', event.value)
				if event.value < -0.01:
					ActiveColor = BLUE
				elif event.value > 0.01:
					ActiveColor = RED
			elif event.axis == 3:
				katety_raw = event.value
			elif event.axis == 4:
				katetx_raw = event.value


	hyp = math.sqrt(katetx_raw * katetx_raw + katety_raw * katety_raw)
	hypscale = 50 / hyp
	katetx = katetx_raw * hypscale
	katety = katety_raw * hypscale

	players[player].setSpeed(dx,dy)
	'''
	aimx = mainRect.centerx + katetx;
	aimy = mainRect.centery + katety;
	aimRect = pygame.Rect(aimx,aimy,3,3)
	'''

	for i in range(0, noOfPlayers):
		players[i].move()
		pygame.draw.rect(DISPLAYSURF, ActiveColor, players[i].rect)
	#pygame.draw.rect(DISPLAYSURF, ActiveColor, aimRect)

	pygame.display.update()
	fpsClock.tick(FPS)