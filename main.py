from sudoku_board import BOARDS, show_process
from pprint import pprint

solved = []
blacklisted = []

boards = BOARDS
board = None


def get_empty_cell():
    for key, row in enumerate(board):
        for cell_key, cell in enumerate(row):
            if cell == 0:
                return key, cell_key # board[row][cell]
    return ()


def get_box(cell_coordinates):
    # Cell, Row
    box_x = 0
    box_y = 0 

    box = []
    row, cell = cell_coordinates
    if row <= 2:
        box_y = 1 

    elif row <= 5:
        box_y = 2

    elif row <= 8:
        box_y = 3
    
    if cell <= 2:
        box_x = 1
    
    elif cell <= 5:
        box_x = 2
    
    elif cell <= 8:
        box_x = 3

    box_x *= 3
    box_y *= 3

    for i in range(3):
        for h in range(3):
            box.append(board[box_y - (h + 1)][box_x - (i + 1)])

    return box

def get_column(cell_coordinates):
    column = []
    for row in board:
        column.append(row[cell_coordinates[1]])

    return column


def check_validity(cell_coordinates, num):
    if num not in get_box(cell_coordinates) and num not in board[cell_coordinates[0]] and num not in get_column(cell_coordinates):
        return True
    return False


def check_blacklisted(cell_coordinates, num):
    for i in blacklisted:
        if i[0] == cell_coordinates:
            if num in i[1]:
                return True
    return False

def check_in_blacklisted(cell_coordinates):
    for key, i in enumerate(blacklisted):
        if i[0] == cell_coordinates:
            return True, key
    return False, 0


if __name__ == '__main__':
    for board_key, i in enumerate(boards):
        blacklisted.clear()
        solved.clear()
        board = i
        while True:
            if show_process:
                pprint(board)
            empty_cell = get_empty_cell()
            if empty_cell != ():
                for i in range(1, 10):
                    if not check_blacklisted(empty_cell, i):
                        valid = check_validity(empty_cell, i)
                        if valid:
                            board[empty_cell[0]][empty_cell[1]] = i

                            in_blacklisted = check_in_blacklisted(empty_cell)
                            if in_blacklisted[0]:
                                blacklisted[in_blacklisted[1]][1].append(i)
                            elif not in_blacklisted[0]:
                                blacklisted.append([empty_cell, [i]])

                            solved.append(empty_cell)
                            break

                if board[empty_cell[0]][empty_cell[1]] == 0:
                    board[solved[-1][0]][solved[-1][1]] = 0
                    in_blacklisted = check_in_blacklisted(empty_cell)
                    if in_blacklisted[0]:
                        blacklisted.pop(in_blacklisted[1])
                    solved.pop(-1)
            elif empty_cell == ():
                boards[board_key] = board
                break

    for k in boards:
        print("")
        print("====SOLUTION====")
        pprint(k)
