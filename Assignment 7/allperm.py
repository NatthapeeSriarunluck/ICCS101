# Assignment 07, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:30 hrs

def all_perm(n: int) -> set[tuple[int, ...]]:
    if n == 1:
        return {(1,)}
    else:
        ans = set()
        for i in all_perm(n - 1):
            for index in range(len(i)+1):
                ans.add(i[0:index] + (n,) + i[index:])
        return ans


assert set(all_perm(1)) == {(1,)}
assert set(all_perm(2)) == {(1, 2), (2, 1)}
assert set(all_perm(3)) == {(3, 1, 2), (1, 3, 2), (1, 2, 3), (3, 2, 1), (2, 3, 1), (2, 1, 3)}
assert set(all_perm(4)) == {(4, 3, 1, 2), (3, 4, 1, 2), (3, 1, 4, 2), (3, 1, 2, 4),
                            (4, 1, 3, 2), (1, 4, 3, 2), (1, 3, 4, 2), (1, 3, 2, 4),
                            (4, 1, 2, 3), (1, 4, 2, 3), (1, 2, 4, 3), (1, 2, 3, 4),
                            (4, 3, 2, 1), (3, 4, 2, 1), (3, 2, 4, 1), (3, 2, 1, 4),
                            (4, 2, 3, 1), (2, 4, 3, 1), (2, 3, 4, 1), (2, 3, 1, 4),
                            (4, 2, 1, 3), (2, 4, 1, 3), (2, 1, 4, 3), (2, 1, 3, 4)}
