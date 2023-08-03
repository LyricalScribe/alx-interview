#!/usr/bin/python3
"""Using Backtracking to Solve N Queens"""
import sys


def nqueens(N, row, board):
    """
    Returns all possible solutions to
    placement, in list of lists
    """
    for col in range(N):
        hold = 0
        for queen in board:
            if col == queen[1]:
                hold = 1
                break
            if row - col == queen[0] - queen[1]:
                hold = 1
                break
            if col - queen[1] == queen[0] - row:
                hold = 1
                break
        if hold == 0:
            board.append([row, col])
            if row != N - 1:
                nqueens(N, row + 1, board)
            else:
                print(board)
            del board[-1]


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except Exception:
        print('N must be a number')
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(N, 0, [])

if __name__ == '__main__':
    main()
