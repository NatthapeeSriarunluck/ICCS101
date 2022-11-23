# Assignment 04, Task 06
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 06:00 hrs

def sumOfDigitsSquared(n: int) -> int:
    ans = 0
    for x in str(n):
        ans += int(x) ** 2
    return ans


def isHappy(n: int) -> bool:
    ans = n
    while (ans != 1) and (ans != 4):
        ans = sumOfDigitsSquared(ans)
    if ans == 1:
        return True
    elif ans == 4:
        return False


def kThHappy(k: int) -> int:
    happy = 0
    num_of_happy = 0
    candidate = 1
    while num_of_happy < k:
        if isHappy(candidate):
            happy = candidate
            num_of_happy += 1
        candidate += 1
    return happy


print(kThHappy(5))