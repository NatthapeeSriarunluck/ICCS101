# Assignment 05, Task 5
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 08: 30 hrs

def word_sleuth(grid: list[list[str]], words: list[str]):
    ans = []
    for i in words:
        if contains_word(grid, i):
            ans.append(i)
    return list(set(ans))


def contains_word(grid: list[list[str]], w: str) -> bool:
    if left_right(grid, w):
        return True
    elif up_down(grid, w):
        return True
    elif diagonal_from_bottomleft_topright(grid, w):
        return True
    elif diagonal_from_topleft_bottomright(grid, w):
        return True
    else:
        return False


def in_square_grid(n: int, x: int, y: int):
    return 0 <= x < n and 0 <= y < n


def sum_helper(grid: list[list[str]], starting_r: int, starting_c: int, dy: int, dx: int) -> str:
    curr, curc = starting_r, starting_c
    ans = ''
    while in_square_grid(len(grid), curr, curc):
        ans += grid[curr][curc]
        curr += dy
        curc += dx
    return ans


def left_right(grid: list[list[str]], w: str) -> bool:
    for r in range(len(grid)):
        read_out = ''
        ans = sum_helper(grid, r, 0, 0, 1)
        read_out += ans
        if w in read_out:
            return True
    return False


def up_down(grid: list[list[str]], w: str) -> bool:
    for r in range(len(grid)):
        read_out = ''
        ans = sum_helper(grid, 0, r, 1, 0)
        read_out += ans
        if w in read_out:
            return True
    return False


def diagonal_from_bottomleft_topright(grid: list[list[str]], w: str) -> bool:
    for r in range(len(grid)):
        read_out = ''
        ans = sum_helper(grid, r, 0, -1, 1)
        read_out += ans
        if w in read_out:
            return True
    return False


def diagonal_from_topleft_bottomright(grid: list[list[str]], w: str) -> bool:
    for r in range(len(grid)):
        read_out = ''
        ans = sum_helper(grid, r, 0, 1, 1)
        read_out += ans
        if w in read_out:
            return True
    return False


