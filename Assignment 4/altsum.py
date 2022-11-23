# Assignment 04, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:00 hrs

def altSum(lst: list[int]) -> int:
    total = lst[0]
    for num in range(len(lst)):
        if num % 2 == 0:
            total -= lst[num]
        else:
            total += lst[num]
    return total
print(altSum([4,3,5,2]))


def test_altSum():
    assert altSum([4, 3, 5, 2]) == 4
    assert altSum([2, 3, 5]) == 0
    assert altSum([5, 2]) == 7
    assert altSum([1]) == 1
    assert altSum([31, 4, 28, 5, 71]) == -59
    assert altSum([7, 7, 7, 7]) == 14
    assert altSum([]) == 0


test_altSum()
