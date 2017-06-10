#!/usr/local/bin/python3
from time import sleep
from conway import Conway

MAX_ROWS = 40
MAX_COLUMNS = 80
# MAX_ROWS = 9
# MAX_COLUMNS = 9 
# DRAW_BOARD = 0
# BUFFER_BOARD = 1
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

conwayGame = Conway(MAX_COLUMNS, MAX_ROWS)

def draw():
	"Draw the baord."
	global conwayGame

	for y in range(MAX_ROWS):
		for x in range(MAX_COLUMNS):
			print( ' ' if conwayGame.getCell(x, y) == 0 else 'X', end='')
			#print('(x, y, v) (', x, ',', y, ',', boards[DRAW_BOARD][y*MAX_COLUMNS + x], ')')
		print('')
	print( ''.join(['-' for x in range(MAX_COLUMNS)]) )

while True:
	draw()
	conwayGame.tick()
	sleep(0.5)
