from pprint import pprint

show_process = False # If you want to view the board as the computer solves it, change this to 'True' (WARNING: IT WILL SLOW THE PROGRAM DOWN)

BOARDS = []

boards = []

with open("boards.txt", "r") as f:
    for i in f:
        boards.append(i)


for board in boards:
    new_board = []
    for i in range(len(board)):
        if (i + 1) % 9 == 0:
            new_row = []
            for k in range(9):
                cell = int(board[i - k])
                new_row.append(cell)
            new_row.reverse()
            new_board.append(new_row)
    
    BOARDS.append(new_board)