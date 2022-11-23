# Assignment 00, Task 00
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 02:00 hrs


def phoneWord2Num(word: str) -> int:
    if len(word) == 7:
        return int(Letter2Num(word[0]) + Letter2Num(word[1]) + Letter2Num(word[2]) + Letter2Num(word[3]) +
                   Letter2Num(word[4]) + Letter2Num(word[5]) + Letter2Num(word[6]))
    else:
        return 0


def Letter2Num(letter: str) -> str:
    if letter in 'abcABC':
        return '2'
    if letter in 'defDEF':
        return '3'
    if letter in 'ghiGHI':
        return '4'
    if letter in 'jklJKL':
        return '5'
    if letter in 'mnoMNO':
        return '6'
    if letter in 'pqrsPQRS':
        return '7'
    if letter in 'tuvTUV':
        return '8'
    if letter in 'wxyzWXYZ':
        return '9'
