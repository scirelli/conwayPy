#!/usr/local/bin/python3
import pygame
from conway import Conway

pygame.init()
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
BLUE     = (   0,   0, 255)
GRAY     = ( 60, 60, 60)

SCREEN_SIZE	 = (700, 500)
CELL_WIDTH   = 5
CELL_HEIGHT = 5
ROWS         = int(SCREEN_SIZE[1]/CELL_HEIGHT)
COLUMNS      = int(SCREEN_SIZE[0]/CELL_WIDTH)
GRID_COLOR	 = GRAY

screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

key = {
	'ESC': 27
}

def drawGrid(pygame, screen):
	"This should drawt he grid lines on the screen"
	LINE_WIDTH = 1
	offsetX = CELL_WIDTH
	offsetY = CELL_HEIGHT

	for col in range(1, COLUMNS):
		pygame.draw.line(screen, GRID_COLOR, [offsetX, 0], [offsetX, SCREEN_SIZE[1]], LINE_WIDTH)
		offsetX += CELL_WIDTH
	for row in range(1, ROWS):
		pygame.draw.line(screen, GRID_COLOR, [0, offsetY], [SCREEN_SIZE[0], offsetY], LINE_WIDTH)
		offsetY += CELL_HEIGHT

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get(): # User did something
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
		elif event.type == pygame.KEYUP:
			print(event.key)
			if event.key == key['ESC']:
				done = True

	# --- Game logic should go here

	# --- Drawing code should go here
	drawGrid(pygame, screen) 

	# --- Go ahead and update the screen with what we've drawn.
	pygame.display.flip()

	# First, clear the screen to white. Don't put other drawing commands
	# above this, or they will be erased with this command.
	screen.fill(BLACK)

	# --- Limit to 60 frames per second
	clock.tick(60)
