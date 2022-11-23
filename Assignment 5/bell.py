# Assignment 05, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 04:00 hrs

def loveTri(n: int) -> list[list[int]]:
    ans = [[1]]
    sub = []
    for i in range(1, n):
        for j in range(0, i + 1):
            if j == 0:
                sub.append(ans[i - 1][i - 1])
            else:
                sub.append(ans[i - 1][j - 1] + sub[j - 1])
        ans.append(sub)
        sub = []
    return ans


