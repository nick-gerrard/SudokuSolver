#! /usr/bin/python3
import time
from random import *
import pprint
from pathlib import Path
import os
import sys

sys.setrecursionlimit(100000000)
print(sys.getrecursionlimit())

# This is an attempt to create a random sudoku generator
# and an app with the functionality to solve it.
try:
    os.mkdir("SudokuPuzzles")
except:
    print("Folder Already Exists")

SudokuPuzzlesDir = Path("SudokuPuzzles")


def create_blank_baord():
    board = []
    for row_number in range(9):
        row = []
        for col in range(9):
            row.append(0)
        board.append(row)


def print_board(board):
    for row in board:
        print(row)
    print("Board has been successfully printed")


# Defining functions to get row, column, and square. Note that
# the row, col, and square numbers will be in range(0-8) NOT
# range(1-9)


def get_value(row, col):
    value = []
    value.append(board[row][col])
    return value


def get_row(row_number):
    return board[row_number]


def get_col(col_number):
    column = []
    for i in range(9):
        column.append(board[i][col_number])
    return column


def get_square(row_number, col_number):
    square = []
    square_col_row = []
    first_row = [0, 1, 2]
    second_row = [3, 4, 5]
    third_row = [6, 7, 8]

    square_number = [first_row, second_row, third_row]

    first_col = [0, 3, 6]
    second_col = [1, 4, 7]
    third_col = [2, 5, 8]

    # Determining which row of squares

    if row_number in first_row:
        square_col_row.append(0)

    elif row_number in second_row:
        square_col_row.append(1)

    elif row_number in third_row:
        square_col_row.append(2)

    # Determining which column of squares

    if col_number in first_row:
        square_col_row.append(0)

    elif col_number in second_row:
        square_col_row.append(1)

    elif col_number in third_row:
        square_col_row.append(2)

    # Determining correct columns on board

    three_full_rows = []
    for value in square_number[square_col_row[0]]:
        three_full_rows.append(board[value])
    # print(f"three full rows: {three_full_rows}")

    # Slicing appended rows

    for row in three_full_rows:
        for value in square_number[square_col_row[1]]:
            square.append(row[value])

    # Returning Square[]

    return square


# Generating the board index of dynamic values:

def board_indexer(board):
    board_index = []
    board_index_full = [[row_num, col_num] for row_num in range(9) for col_num in range(9)]
    for coordinates in board_index_full:
        if board[coordinates[0]][coordinates[1]] == 0:
            board_index.append(coordinates)
    return board_index


# Function to check value of place

def check_value(coordinates):
    global board
    value = board[coordinates[0]][coordinates[1]]

    # setting value to 1 if un-evaluated (=0)

    if value == 0:
        # board[coordinates[0]][coordinates[1]] = 1
        value = 1  # board[coordinates[0]][coordinates[1]]

    # setting value to 0 if = 9, return false

    if value == 9:
        board[coordinates[0]][coordinates[1]] = 0
        return False

    for number in [1, 2, 3, 4, 5, 6, 7, 8, 9][value - 1:]:
        row = get_row(coordinates[0])
        col = get_col(coordinates[1])
        square = get_square(coordinates[0], coordinates[1])
        if number not in row and number not in col and number not in square:
            board[coordinates[0]][coordinates[1]] = number
            # print(f"Value at {coordinates} has been updated to {board[coordinates[0]][coordinates[1]]}!")
            return True
        elif number == 9:
            # print("resetting number to 0 and recursing back")
            board[coordinates[0]][coordinates[1]] = 0
            new_value = board[coordinates[0]][coordinates[1]]
            # print(f"The value at [{coordinates[0]},{coordinates[1]}] has been reset to {new_value}!")
            return False


# Function to solve, and print, the board

def sudoku_solver(board, board_index, index=0):
    # print(f"The current index is: {index}")
    continue_function = False
    for row in board:
        for value in row:
            if value == 0:
                continue_function = True

    if not continue_function:
        print("Success, the puzzle has been solved!")
        print_board(board)
        return board

    else:
        if check_value(board_index[index]) == True:
            # print("moving to next number")
            new_index = index + 1
            sudoku_solver(board, board_index, new_index)
        else:
            new_index = index - 1
            # print("moving back a number")
            sudoku_solver(board, board_index, new_index)
    return board


def random_unsolved_board(solved_board):
    for row in range(9):
        for col in range(9):
            random_value = randint(1, 10)
            if random_value > 2:
                solved_board[row][col] = 0
    # print_board(solved_board)
    return solved_board


'''board = [ 
                [4,0,0,1,0,2,6,8,0],
                [1,0,0,0,9,0,0,0,4],
                [0,3,8,0,6,4,0,1,0],
                [0,0,5,0,7,1,9,2,0],
                [0,2,6,0,0,9,8,0,0],
                [8,0,0,2,5,0,0,0,0],
                [9,0,3,0,0,0,0,0,8],
                [2,5,0,6,0,0,1,0,7],
                [6,0,7,9,0,5,3,0,0]
                ]
                '''

board = [
    [6, 0, 0, 1, 5, 7, 0, 0, 0],
    [3, 0, 0, 2, 0, 4, 0, 9, 0],
    [0, 1, 0, 0, 0, 6, 0, 4, 0],
    [2, 6, 0, 0, 1, 0, 8, 0, 3],
    [5, 0, 0, 0, 0, 0, 9, 2, 4],
    [0, 0, 3, 9, 0, 0, 0, 0, 5],
    [1, 3, 0, 6, 0, 2, 0, 0, 0],
    [9, 4, 6, 8, 3, 1, 7, 0, 0],
    [7, 0, 0, 0, 4, 9, 0, 1, 0]

]

board_index = board_indexer(board)


'''try:
    solved_board = sudoku_solver(board, board_index)
except:
    print("uhoh")



print_board(solved_board)
# Generating random boardss


# print("Random Unsolved Board Generated! \n")
unsolved_board = random_unsolved_board(solved_board)

index2 = board_indexer(unsolved_board)
try:
    solved_board2 = sudoku_solver(unsolved_board, index2)
except:
    print("recursion error")
#print_board(solved_board2)
'''