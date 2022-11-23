# Assignment 6, Task 6
# Name: Natthapee Sriarunluck
# Collaborators:
# Time Spent: 4:00 hrs
# ----------------------------------

from re import I


Board = list[list[str]]


def isGameOver(board: Board) -> bool:
    if emptyPos(board) == [] and (doKeyUp(board)[0] == False) and (doKeyDown(board)[0] == False) and (
            doKeyRight(board)[0] == False) and (doKeyLeft(board)[0] == False):
        return True
    else:
        return False


def doKeyUp(board: Board) -> tuple[bool, Board]:
    change = False
    for i in range(1, len(board)):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                k = i
                while k - 1 >= 0:
                    if board[k - 1][j] == ' ':
                        board[k - 1][j] = board[k][j]
                        board[k][j] = ' '
                        change = True
                    k -= 1
            continue
    for i in range(len(board) - 1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                if board[i][j] != board[i - 1][j]:
                    continue
                else:
                    board[i][j] = str(int(board[i][j]) + int(board[i - 1][j]))
                    board[i - 1][j] = ' '
                    change = True
    for i in range(1, len(board)):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                k = i
                while k - 1 >= 0:
                    if board[k - 1][j] == ' ':
                        board[k - 1][j] = board[k][j]
                        board[k][j] = ' '
                        change = True
                    k -= 1

            continue
    return change, board


def doKeyDown(board: Board) -> tuple[bool, Board]:
    change = False
    for i in range(len(board) - 2, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                k = i
                while k + 1 < len(board):
                    if board[k + 1][j] == ' ':
                        board[k + 1][j] = board[k][j]
                        board[k][j] = ' '
                        change = True
                    k += 1
            continue
    for j in range(len(board[0])):
        for i in range(len(board) - 1):
            if board[i][j] != ' ':
                if board[i][j] != board[i + 1][j]:
                    continue
                else:
                    board[i][j] = str(int(board[i][j]) + int(board[i + 1][j]))
                    board[i + 1][j] = ' '
                    change = True
    for i in range(len(board) - 2, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] != ' ':
                k = i
                while k + 1 < len(board):
                    if board[k + 1][j] == ' ':
                        board[k + 1][j] = board[k][j]
                        board[k][j] = ' '
                        change = True
                    k += 1
    return change, board


def doKeyLeft(board: Board) -> tuple[bool, Board]:
    change = False
    for j in range(1, len(board[0])):
        for i in range(len(board)):
            if board[i][j] != ' ':
                k = j
                while k - 1 >= 0:
                    if board[i][k - 1] == ' ':
                        board[i][k - 1] = board[i][k]
                        board[i][k] = ' '
                        change = True
                    k -= 1
            continue
    for i in range(len(board)):
        for j in range(len(board[0]) -1, - 1, -1):
            if board[i][j] != ' ':
                if board[i][j] != board[i][j - 1]:
                    continue
                else:
                    board[i][j] = str(int(board[i][j]) + int(board[i][j - 1]))
                    board[i][j - 1] = ' '
                    change = True
    for j in range(1, len(board[0])):
        for i in range(len(board)):
            if board[i][j] != ' ':
                k = j
                while k - 1 >= 0:
                    if board[i][k - 1] == ' ':
                        board[i][k - 1] = board[i][k]
                        board[i][k] = ' '
                        change = True
                    k -= 1
    return change, board


def doKeyRight(board: Board) -> tuple[bool, Board]:
    change = False
    for j in range(len(board[0]) - 2, -1, -1):
        for i in range(len(board)):
            if board[i][j] != ' ':
                k = j
                while k + 1 < len(board[0]):
                    if board[i][k + 1] == ' ':
                        board[i][k + 1] = board[i][k]
                        board[i][k] = ' '
                        change = True
                    k += 1
            continue
    for i in range(len(board)):
        for j in range(len(board[0]) - 1):
            if board[i][j] != ' ':
                if board[i][j] != board[i][j + 1]:
                    continue
                else:
                    board[i][j] = str(int(board[i][j]) + int(board[i][j + 1]))
                    board[i][j + 1] = ' '
                    change = True
    for j in range(len(board[0]) - 2, -1, -1):
        for i in range(len(board)):
            if board[i][j] != ' ':
                k = j
                while k + 1 < len(board[0]):
                    if board[i][k + 1] == ' ':
                        board[i][k + 1] = board[i][k]
                        board[i][k] = ' '
                        change = True
                    k += 1
    return change, board


def emptyPos(board: Board) -> list[tuple[int, int]]:
    ans = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                ans.append((i, j))
    return ans

