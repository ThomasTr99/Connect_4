import numpy as np

ROW_COUNT = 6
COL_COUNT = 7

def create_board():
    #Will create a board of zeros with 6 rows and 7 columns and return it
    board = np.zeros((6,7))
    return board

def drop_piece(board, row, col, piece):
    #The piece will be dropped at the user inputted space and assign it
    board[row][col] = piece

def is_valid_location(board, col):
    #Check to see if that row is open
    return board[5][col] == 0

def get_next_open_row(board, col):
    #the loop checks the range of the boards rows and if the position of the column is free(0), then it returns that position
    for i in range(ROW_COUNT):
        if board[i][col] == 0:
            return i

#This function allows the board to be flipped with the numpy method flip() which will force the pieces to be at the bottom instead of the top
def print_board(board):
    print(np.flip(board, 0))

board = create_board()
print_board(board)
game_over = False
turn = 0

while not game_over:
    #Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1: Make Your Selection (0-6): "))
        #First, it checks if that location is open, then gets the next open row, then drops the piece into that selection that the user made
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
    #Ask for Player 2 input
    else:
        col = int(input("Player 2: Make Your Selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
    print_board(board)
    turn += 1
    #This will allow the turn number to alternate between 0 and 1 for each player
    turn = turn % 2


