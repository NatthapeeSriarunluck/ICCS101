# Assignment 04, Task 04
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 05:00 hrs

def readAloud(lst: list[int]) -> list[int]:
    ans = []
    consecutive = 1
    x = 0
    if len(lst) == 0:
        return ans
    if len(lst) == 1:
        ans.extend([1, lst[0]])
        return ans
    while x + 1 < len(lst):
        if lst[x] == lst[x + 1]:
            consecutive += 1
            x += 1
        else:
            ans.extend([consecutive, lst[x]])
            x += 1
            consecutive = 1
            continue
    if lst[-1] == lst[-2]:
        ans.extend([consecutive, lst[-1]])
    else:
        ans.extend([1, lst[-1]])
    return ans


def test_readAloud():
    assert readAloud([1, 1, 1]) == [3, 1]
    assert readAloud([-1, 2, 7]) == [1, -1, 1, 2, 1, 7]
    assert readAloud([3, 3, 1, 1, 3, 1, 1]) == [2, 3, 2, 1, 1, 3, 2, 1]
    assert readAloud([3, 3, 8, -10, -10, -10]) == [2, 3, 1, 8, 3, -10]
    assert readAloud([1, 2]) == [1, 1, 1, 2]
    assert readAloud([1]) == [1, 1]
    assert readAloud([]) == []

# test_readAloud()
