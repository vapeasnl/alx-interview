#!/usr/bin/python3
"""N-Queens puzzle Function"""
import sys


def print_board(board, n):
    """prints nqueen position"""
    b = []

    for i in range(n):
        for j in range(n):
            if j == board[i]:
                b.append([i, j])
    print(b)


def safe_position(board, i, j, r):
    """Function checks if its safe for the nqueen"""
    return board[i] in (j, j - i + r, i - r + j)


def determine_positions(board, row, n):
    """Function wiill find safe places to allocate the nqueen """
    if row == n:
        print_board(board, n)

    else:
        for j in range(n):
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board[row] = j
                determine_positions(board, row + 1, n)


def create_board(size):
    """creates board"""
    return [0 * size for i in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
determine_positions(board, row, int(n))
