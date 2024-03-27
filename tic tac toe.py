import numpy as np
import random
from time import sleep


def create_board():
	return(np.array([[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]]))
#This function returns a list of tuples representing the positions where a player can make a move 
#(i.e., positions that are currently empty).
def possibilities(board):
	l = []

	for i in range(len(board)):
		for j in range(len(board)):

			if board[i][j] == 0:
				l.append((i, j))
	return(l)
#This function randomly selects a position on the board where the player can make a move
# and places the player's symbol (either 1 or 2) at that position.
def random_place(board, player):
	selection = possibilities(board)
	current_loc = random.choice(selection)
	board[current_loc] = player
	return(board)

def check_win(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i] == player) or all(board[:, i] == player):
            return True

    # Check diagonals
    if all(np.diag(board) == player) or all(np.diag(np.fliplr(board)) == player):
        return True

    return False

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        if check_win(board, player):
            winner = player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
	board, winner, counter = create_board(), 0, 1
	print(board)
	sleep(2)

	while winner == 0:
		for player in [1, 2]:
			board = random_place(board, player)
			print("Board after " + str(counter) + " move")
			print(board)
			sleep(2)
			counter += 1
			winner = evaluate(board)
			if winner != 0:
				break
	return(winner)

print("Winner is: " + str(play_game()))