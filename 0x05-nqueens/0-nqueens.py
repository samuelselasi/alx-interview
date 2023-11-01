#!/usr/bin/python3
"""Module with solution for the N-Queens challenge with backtracking"""
import sys


def chessboard(pos, n):
    """Function to print chessboard with appropriate positions of queens"""

    board = []

    for RANK in range(n):
        for FILE in range(n):
            if FILE == pos[RANK]:
                board.append([RANK, FILE])

    print(board)


def safe_pos(pos, RANK, FILE, n):
    """Function to determine safe a square to place a queen"""

    if (pos[RANK] == FILE) or (pos[RANK] == FILE - RANK + n) or \
            (pos[RANK] == RANK - n + FILE):
        return True
    return False


def get_safe_pos(board, rank, n):
    """Function to get all safe positions to place queens with recursion"""

    if rank == n:
        chessboard(board, n)
    else:
        for FILE in range(n):
            safe = True

            for RANK in range(rank):
                if safe_pos(board, RANK, FILE, rank):
                    safe = False

            if safe:
                board[rank] = FILE
                get_safe_pos(board, rank + 1, n)


def create_board(n):
    """Function to generate chessboard of n-size"""

    return [0 * n for i in range(n)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except Exception:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)


board = create_board(int(n))
rank = 0
get_safe_pos(board, rank, int(n))
