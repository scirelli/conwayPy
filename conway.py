#!/usr/local/bin/python3
from random import randint, choice
from time import sleep

class Conway:
	LIVE = 1
	DEAD = 0
	UNDERPOPULATION = 2 * LIVE
	OVERPOPULATION = 3 * LIVE
	REPRODUCTION = 3 * LIVE
	DRAW_BOARD = 0
	BUFFER_BOARD = 1

	def __init__(self, maxColumns, maxRows):
		self.maxRows = maxRows
		self.maxColumns = maxColumns
		self.boards = [[choice([DEAD,LIVE,DEAD,DEAD,DEAD,DEAD,DEAD]) for x in range(self.maxRows * self.maxColumns)]] * 2

	def swap(self):
		"Swap the two self.boards in the array. So the buffer becoems the board you draw. And the the baord you draw becomes the buffer."
		tmp = self.boards[DRAW_BOARD]
		self.boards[DRAW_BOARD] = self.boards[BUFFER_BOARD]
		self.boards[BUFFER_BOARD] = tmp

	def tick(self):
		"Do the work!"
		swap()
				
		for y in range(self.maxRows):
			for x in range(self.maxColumns):
				liveCount = 0

				pos = (y-1)*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and x-1 >= 0 and y-1 >= 0:
					liveCount += self.boards[BUFFER_BOARD][pos]
				pos = (y-1)*self.maxColumns + x
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and y-1 >= 0:
					liveCount += self.boards[BUFFER_BOARD][pos]
				pos = (y-1)*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and y-1 >= 0 and x+1 < self.maxColumns:
					liveCount += self.boards[BUFFER_BOARD][pos]
				
				pos = y*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and x-1 >= 0:
					liveCount += self.boards[BUFFER_BOARD][pos]
				pos = y*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and x+1 < self.maxColumns:
					liveCount += self.boards[BUFFER_BOARD][pos]
				
				pos = (y+1)*self.maxColumns + (x-1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and y+1 < self.maxRows and x-1 >= 0:
					liveCount += self.boards[BUFFER_BOARD][pos]
				pos = (y+1)*self.maxColumns + x
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and y+1 < self.maxRows:
					liveCount += self.boards[BUFFER_BOARD][pos]
				pos = (y+1)*self.maxColumns + (x+1)
				if pos >= 0 and pos < len(self.boards[BUFFER_BOARD]) and y+1 < self.maxRows and x+1 < self.maxColumns:
					liveCount += self.boards[BUFFER_BOARD][pos]

				value = self.boards[BUFFER_BOARD][y*self.maxColumns + x]
				if value == LIVE:
					if (liveCount < UNDERPOPULATION) or (liveCount > OVERPOPULATION):
						self.boards[DRAW_BOARD][y*self.maxColumns + x] = DEAD
					else:
						#Remain alive
						self.boards[DRAW_BOARD][y*self.maxColumns + x] = LIVE
				else:
					if liveCount == REPRODUCTION:
						self.boards[DRAW_BOARD][y*self.maxColumns + x] = LIVE
					else:
						#remain dead
						self.boards[DRAW_BOARD][y*self.maxColumns + x] = DEAD

	def getBoard(self):
		return self.boards[DRAW_BOARD]
