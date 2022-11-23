# Assignment 05, Task 03
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 02:30 hrs
import math


def table(msg: str, key: int) -> list[list[str]]:
    row = math.ceil(len(msg) / key)
    column = key
    new = msg + '_' * (row * column - len(msg))
    main = []
    i = 0
    index = 0
    while i < row:
        j = 0
        sub = []
        while j < column:
            sub.append(new[index])
            index += 1
            j += 1
        main.append(sub)
        i += 1
    return main


def enc(msg: str, key: int) -> str:
    msg_table = table(msg, key)
    ans = ''
    for j in range(key):
        for i in range(len(msg_table)):
            if msg_table[i][j] != '_':
                ans += msg_table[i][j]
    return ans

