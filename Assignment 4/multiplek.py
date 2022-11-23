# Assignment 04, Task 05
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:20 hrs

def allMultiplesOfK(k: int, lst: list[int]) -> bool:
    if len(lst) == 0:
        return True
    for x in range(len(lst)):
        if lst[x] % k == 0:
            continue
        else:
            return False
    return True

def test_allMultiplesOfK():
    assert allMultiplesOfK(4, [1, 10, 20]) == False
    assert allMultiplesOfK(3, [81,3,24]) == True
    assert allMultiplesOfK(11, []) == True
    assert allMultiplesOfK(2, [4]) == True

test_allMultiplesOfK()