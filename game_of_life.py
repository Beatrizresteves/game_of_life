class Solution:
	def gameOfLife(self, board: List[List[int]]) -> None:
		# Original | New | State
		#    0     |  0  |   0  
		#    1     |  0  |   1  
		#    0     |  1  |   1  
		#    1     |  1  |   3  

		ROWS, COLS = len(board), len(board[0])

		for r in range(ROWS):
			for c in range(COLS):
				nei = countNeighbors(r, c)

				if board[r][c]:
					if nei in [2, 3]:
						board[r][c] = 3
				elif nei == 3:
						board[r][c] = 2
		
		for r in range(ROWS):
			for c in range(COLS):