# This is the 3 player version
import numpy as np
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)
GREEN = (3,252,90)

ROW_COUNT_in = 0

while ROW_COUNT_in < 5 or ROW_COUNT_in > 10:
	print("Enter a number of rows between 5 and 10")
	ROW_COUNT_in = input("Number of Rows: ")
	ROW_COUNT_in = int(ROW_COUNT_in)

COLUMN_COUNT_in = 0

while COLUMN_COUNT_in < 5 or COLUMN_COUNT_in > 10:
	print("Enter a number of columns between 5 and 10")
	COLUMN_COUNT_in = input(" Number of Column: ")
	COLUMN_COUNT_in = int(COLUMN_COUNT_in)

Num_Connections_in = 0

while Num_Connections_in < 3 or Num_Connections_in > 5:
	print("Enter number of required connections between 3-5 ")
	Num_Connections_in= input("required connections: ")
	Num_Connections_in= int(Num_Connections_in)


ROW_COUNT = int(ROW_COUNT_in)
COLUMN_COUNT = int(COLUMN_COUNT_in)
NUM_CONNECT = int(Num_Connections_in)


def create_board():
	board = np.zeros((ROW_COUNT,COLUMN_COUNT))
	return board

def drop_piece(board, row, col, piece):
	board[row][col] = piece

def is_valid_location(board, col):
	return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
	for r in range(ROW_COUNT):
		if board[r][col] == 0:
			return r

def print_board(board):
	print(np.flip(board, 0))

def winning_move(board, piece):  
# Check horizontal locations for win
    if NUM_CONNECT==5:
    	for c in range(COLUMN_COUNT-4):
	    	for r in range(ROW_COUNT):
		    	if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece and board[r][c+4] == piece:
			    	return True

    elif NUM_CONNECT==4:
    	for c in range(COLUMN_COUNT-3):
	    	for r in range(ROW_COUNT):
		    	if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
			    	return True

    else:
    	for c in range(COLUMN_COUNT-2):
	    	for r in range(ROW_COUNT):
		    	if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece:
			    	return True

	# Check vertical locations for win
    if NUM_CONNECT==5:
	    for c in range(COLUMN_COUNT):
    	    	for r in range(ROW_COUNT-4):
	    	    	if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece and board[r+4][c] == piece:
		    	    	return True

    elif NUM_CONNECT==4:
	    for c in range(COLUMN_COUNT):
    	    	for r in range(ROW_COUNT-3):
	    	    	if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
		    	    	return True

    else:
	    for c in range(COLUMN_COUNT):
    	    	for r in range(ROW_COUNT-2):
	    	    	if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece:
		    	    	return True


	# Check positively sloped diaganols
    if NUM_CONNECT==5:
        for c in range(COLUMN_COUNT-4):
     	    for r in range(ROW_COUNT-4):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece and board[r+4][c+4] == piece:
                    return True

    elif NUM_CONNECT==4:
        for c in range(COLUMN_COUNT-3):
     	    for r in range(ROW_COUNT-3):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                    return True

    else:
        for c in range(COLUMN_COUNT-2):
     	    for r in range(ROW_COUNT-2):
                if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece:
                    return True


	# Check negatively sloped diaganols
    if NUM_CONNECT==5:
	    for c in range(COLUMN_COUNT-4):
    		for r in range(4, ROW_COUNT):
	    		if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece and board[r-4][c+4]:
		    		return True

    elif NUM_CONNECT==4:
	    for c in range(COLUMN_COUNT-3):
    		for r in range(3, ROW_COUNT):
	    		if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
		    		return True

    else:
	    for c in range(COLUMN_COUNT-2):
    		for r in range(2, ROW_COUNT):
	    		if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece:
		    		return True


def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), RADIUS)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, GREEN, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)
			elif board[r][c] == 3:
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), height-int(r*SQUARESIZE+SQUARESIZE/2)), RADIUS)

	pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0
count = 0

pygame.init()

SQUARESIZE = 50

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 45)

while not game_over:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.MOUSEMOTION:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			posx = event.pos[0]
			if turn == 0:
				pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
			elif turn == 1:
			    pygame.draw.circle(screen, GREEN, (posx, int(SQUARESIZE/2)), RADIUS)
			else:
				pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
		pygame.display.update()

		if event.type == pygame.MOUSEBUTTONDOWN:
			pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
			#print(event.pos)
			# Ask for Player 1 Input
			if turn == 0:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 1)

					if winning_move(board, 1):
						label = myfont.render("Player 1 wins!!", 1, RED)
						screen.blit(label, (40,5))
						game_over = True

			# Ask for Player 2 Input
			elif turn == 1:
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 2)

					if winning_move(board, 2):
						label = myfont.render("Player 2 wins!!", 1, GREEN)
						screen.blit(label, (40,5))
						game_over = True
			
			# # Ask for Player 3 Input
			else:				
				posx = event.pos[0]
				col = int(math.floor(posx/SQUARESIZE))

				if is_valid_location(board, col):
					row = get_next_open_row(board, col)
					drop_piece(board, row, col, 3)

					if winning_move(board, 3):
						label = myfont.render("Player 3 wins!!", 1, YELLOW)
						screen.blit(label, (40,5))
						game_over = True

			print_board(board)
			draw_board(board)

			count = count + 1
			if count == (ROW_COUNT*COLUMN_COUNT+1) and game_over == False:
				game_over = True
				label = myfont.render("Tie! Try Again", 1, BLACK)
				screen.blit(label, (40,5))
			print_board(board)
			draw_board(board)


			if turn==0:
				turn=1
				print("turn was 0")
			elif turn==1:
				turn=2
				print("turn was 1")
			else:
				turn=0
				print("turn was 2")


#			turn += 1
#			turn = turn % 2

			if game_over:
				pygame.time.wait(3000)
