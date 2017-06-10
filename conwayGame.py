#!/usr/local/bin/python3
from random import randint, choice
from time import sleep

LIVE = 1
DEAD = 0
UNDERPOPULATION = 2 * LIVE
OVERPOPULATION = 3 * LIVE
REPRODUCTION = 3 * LIVE
MAX_ROWS = 40
MAX_COLUMNS = 80
DRAW_BOARD = 0
BUFFER_BOARD = 1

#boards = [[randint(DEAD, LIVE) for x in range(MAX_ROWS * MAX_COLUMNS)]] * 2
boards = [[choice([DEAD,LIVE,DEAD,DEAD,DEAD,DEAD,DEAD]) for x in range(MAX_ROWS * MAX_COLUMNS)]] * 2
# MAX_ROWS = 9
# MAX_COLUMNS = 9 
# boards[DRAW_BOARD] = [
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,1,1,1,0,0,0,
# 	0,0,0,1,1,1,0,0,0,
# 	0,0,0,1,1,1,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0
# ]
# boards[BUFFER_BOARD] = [
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0,
# 	0,0,0,0,0,0,0,0,0
# ]

def swap():
	"Swap the two boards in the array. So the buffer becoems the board you draw. And the the baord you draw becomes the buffer."
	global boards
	tmp = boards[DRAW_BOARD]
	boards[DRAW_BOARD] = boards[BUFFER_BOARD]
	boards[BUFFER_BOARD] = tmp

def draw():
	"Draw the baord."
	global boards

	for y in range(MAX_ROWS):
		for x in range(MAX_COLUMNS):
			print( ' ' if boards[DRAW_BOARD][y*MAX_COLUMNS + x] == 0 else 'X', end='')
			#print('(x, y, v) (', x, ',', y, ',', boards[DRAW_BOARD][y*MAX_COLUMNS + x], ')')
		print('')
	print( ''.join(['-' for x in range(MAX_COLUMNS)]) )

def tick():
	"Do the work!"
	global boards
	swap()
            
	for y in range(MAX_ROWS):
		for x in range(MAX_COLUMNS):
			liveCount = 0

			pos = (y-1)*MAX_COLUMNS + (x-1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and x-1 >= 0 and y-1 >= 0:
				liveCount += boards[BUFFER_BOARD][pos]
			pos = (y-1)*MAX_COLUMNS + x
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and y-1 >= 0:
				liveCount += boards[BUFFER_BOARD][pos]
			pos = (y-1)*MAX_COLUMNS + (x+1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and y-1 >= 0 and x+1 < MAX_COLUMNS:
				liveCount += boards[BUFFER_BOARD][pos]
			
			pos = y*MAX_COLUMNS + (x-1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and x-1 >= 0:
				liveCount += boards[BUFFER_BOARD][pos]
			pos = y*MAX_COLUMNS + (x+1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and x+1 < MAX_COLUMNS:
				liveCount += boards[BUFFER_BOARD][pos]
			
			pos = (y+1)*MAX_COLUMNS + (x-1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and y+1 < MAX_ROWS and x-1 >= 0:
				liveCount += boards[BUFFER_BOARD][pos]
			pos = (y+1)*MAX_COLUMNS + x
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and y+1 < MAX_ROWS:
				liveCount += boards[BUFFER_BOARD][pos]
			pos = (y+1)*MAX_COLUMNS + (x+1)
			if pos >= 0 and pos < len(boards[BUFFER_BOARD]) and y+1 < MAX_ROWS and x+1 < MAX_COLUMNS:
				liveCount += boards[BUFFER_BOARD][pos]

			value = boards[BUFFER_BOARD][y*MAX_COLUMNS + x]
			if value == LIVE:
				if (liveCount < UNDERPOPULATION) or (liveCount > OVERPOPULATION):
					boards[DRAW_BOARD][y*MAX_COLUMNS + x] = DEAD
				else:
					#Remain alive
					boards[DRAW_BOARD][y*MAX_COLUMNS + x] = LIVE
			else:
				if liveCount == REPRODUCTION:
					boards[DRAW_BOARD][y*MAX_COLUMNS + x] = LIVE
				else:
					#remain dead
					boards[DRAW_BOARD][y*MAX_COLUMNS + x] = DEAD

while True:
	#print(boards[0])
	draw()
	tick()
	sleep(0.5)
