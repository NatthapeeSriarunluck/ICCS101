# Assignment 00, Task 00
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 80:00 hrs

def is_prime(n: int) -> bool:
    if n == 2:
        return True
    elif n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    else:
        return False



def test_is_prime():
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(-2) == False
    assert is_prime(5) == True
    assert is_prime(41) == True
    assert is_prime(323) == False
    assert is_prime(0) == False


# test_is_prime()

def sans_primes(numbers: list[int]) -> list[int]:
    new_list = []
    x = 0
    y = len(numbers)
    while x < y:
        if is_prime(numbers[x]):
            x += 1
            continue
        if x != 0:
            if is_prime(numbers[x - 1]):
                x += 1
                continue
        new_list.append(numbers[x])
        x += 1
    return new_list


def test_sans_primes():
    assert sans_primes([1, 4, 9, 10]) == [1, 4, 9, 10]
    assert sans_primes([1, 11, 9, 10, 17]) == [1, 10]
    assert sans_primes([3, 10, 2, 8, 9, 4, 1, 7, 6, 5, 11]) == [9, 4, 1]
    assert sans_primes([3, 1, 2, 4]) == []
    assert sans_primes([3, -2, 5, 7, 1, 42]) == [42]
    assert sans_primes([1, 0, 3, 0, -2, 5, 7, 1, 42, 9]) == [1, 0, -2, 42, 9]
#test_sans_primes()
