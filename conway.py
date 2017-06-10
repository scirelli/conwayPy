#!/usr/local/bin/python3
from random import randint, choice
from time import sleep

class Conway:
	"""
	Rules to Conway's Game of Life
	1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
	2. Any live cell with two or three live neighbours lives on to the next generation.
	3. Any live cell with more than three live neighbours dies, as if by overpopulation.
	4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
	"""
	LIVE = 1
	DEAD = 0
	UNDERPOPULATION = 2 * LIVE
	OVERPOPULATION = 3 * LIVE
	REPRODUCTION = 3 * LIVE
	DRAW_BOARD = 0
	BUFFER_BOARD = 1
	TEST_ROWS = 9
	TEST_COLUMNS = 9

	PATTERNS = [
		[
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0
		],
		[
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,1,1,1,0,0,0,
			0,0,0,1,1,1,0,0,0,
			0,0,0,1,1,1,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0
		],
		[
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,1,
			0,0,0,0,0,0,0,0,1,
			0,0,0,0,0,0,0,0,1,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0,
			0,0,0,0,0,0,0,0,0
		],
		[
			1,1,1,1,1,1,1,1,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,0,0,0,0,0,0,0,1,
			1,1,1,1,1,1,1,1,1
		]
	]

	def __init__(self, maxColumns, maxRows):
		self.maxColumns = maxColumns
		self.maxRows = maxRows
		self.boards = [
						[
							choice(
								[
									Conway.LIVE
									,Conway.DEAD
									,Conway.DEAD
									,Conway.DEAD
									,Conway.DEAD
									#,Conway.DEAD
									#,Conway.DEAD
									#,Conway.DEAD
									#,Conway.DEAD
									#,Conway.DEAD
								]
							) for x in range(self.maxRows * self.maxColumns)
						],
						[0 for x in range(self.maxRows * self.maxColumns)]
					  ] # * 2
	
	def test(self):
		"A simple board to test with."

		self.maxColumns = Conway.TEST_COLUMNS
		self.maxRows = Conway.TEST_ROWS
		
		self.boards[Conway.DRAW_BOARD] = Conway.PATTERNS[3]
		self.boards[Conway.BUFFER_BOARD] = Conway.PATTERNS[0]

	def swap(self):
		"Swap the two self.boards in the array. So the buffer becoems the board you draw. And the the baord you draw becomes the buffer."
		tmp = self.boards[Conway.DRAW_BOARD]
		self.boards[Conway.DRAW_BOARD] = self.boards[Conway.BUFFER_BOARD]
		self.boards[Conway.BUFFER_BOARD] = tmp

	def tick(self):
		"Do the work!"
		self.swap()
				
		for y in range(self.maxRows):
			for x in range(self.maxColumns):
				liveCount = 0

				pos = (y-1)*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and x-1 >= 0 and y-1 >= 0:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				pos = (y-1)*self.maxColumns + x
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and y-1 >= 0:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				pos = (y-1)*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and y-1 >= 0 and x+1 < self.maxColumns:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				
				pos = y*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and x-1 >= 0:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				pos = y*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and x+1 < self.maxColumns:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				
				pos = (y+1)*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and y+1 < self.maxRows and x-1 >= 0:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				pos = (y+1)*self.maxColumns + x
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and y+1 < self.maxRows:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]
				pos = (y+1)*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[Conway.BUFFER_BOARD]) and y+1 < self.maxRows and x+1 < self.maxColumns:
					liveCount += self.boards[Conway.BUFFER_BOARD][pos]

				value = self.boards[Conway.BUFFER_BOARD][y*self.maxColumns + x]
				if value == Conway.LIVE:
					if (liveCount < Conway.UNDERPOPULATION) or (liveCount > Conway.OVERPOPULATION):
						self.boards[Conway.DRAW_BOARD][y*self.maxColumns + x] = Conway.DEAD
					else:
						#Remain a Conway.LIVE
						self.boards[Conway.DRAW_BOARD][y*self.maxColumns + x] = Conway.LIVE
				else:
					if liveCount == Conway.REPRODUCTION:
						self.boards[Conway.DRAW_BOARD][y*self.maxColumns + x] = Conway.LIVE
					else:
						#remain Conway.DEAD
						self.boards[Conway.DRAW_BOARD][y*self.maxColumns + x] = Conway.DEAD

	def getBoard(self):
		return self.boards[Conway.DRAW_BOARD]

	def getCell(self, x, y):
		return self.boards[Conway.DRAW_BOARD][y*self.maxColumns + x]
