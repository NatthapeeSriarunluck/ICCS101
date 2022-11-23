# Assignment 03, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:00 hr

def my_min(p: float, q: float, r: float) -> float:
    if p < q and p < r:
        return p
    elif q < p and q < r:
        return q
    else:
        return r


def my_mean(p: float, q: float, r: float) -> float:
    return 1 / 3 * (p + q + r)


def my_med(p: float, q: float, r: float) -> float:
    if (q < p < r) or (q > p > r):
        return p
    if (p < q < r) or (p > q > r):
        return q
    if (p < r < q) or (p > r > q):
        return r
