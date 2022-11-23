# Assignment 06, Task 04
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:40 hrs

def eto(lst: list[int]) -> list[int]:
    if lst == []:
        return []
    else:
        if lst[0] % 2 == 0:
            return [lst[0]] + eto(lst[1:])
        else:
            return eto(lst[1:]) + [lst[0]]


assert eto([]) == []
assert set(eto([3, 1, 2])) == {2, 1, 3}
assert set(eto([4, 2, 8])) == {8, 4, 2}
assert set(eto([8, -2, 3, -3, -1, 5, 8, -1, 5])) == {8, -2, 8, 5, -1, 5, -1, -3, 3}
assert set(eto([1])) == {1}
assert set(eto([2])) == {2}
assert set(eto([1, 3])) == {1, 3}
assert set(eto([3, 1])) == {1, 3}
assert set(eto([1, 2])) == {2,1}
assert set(eto([8, 1, 2])) == {2, 8, 1}
