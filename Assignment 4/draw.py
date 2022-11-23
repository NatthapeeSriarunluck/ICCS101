# Assignment 04, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 03:00 hrs

def triangle(k: int) -> None:
    for i in range(1, k + 1):
        print(f'{"#" * (k - i)}{"*" * (2 * i - 1)}{"#" * (k - i)}')


def diamond(k: int) -> None:
    for i in range(1, k + 1):
        print(f'{"#" * (k + 1 - i)}{"*" * (2 * i - 1)}{"#" * (k + 1 - i)}') 
    for i in range(1, k + 1):
        print(f'{"#" * i}{"*" * (2 * k + 1 - 2 * i)}{"#" * i}')


print(diamond(2))