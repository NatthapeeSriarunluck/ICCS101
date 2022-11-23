def altSum(lst: list[int]) -> int:
    if not lst:
        return 0
    total = lst[0]
    for index in range(len(lst)):
        if index == 0:
            continue
        if index % 2 == 0:
            total -= lst[index]
        else:
            total += lst[index]
    return total

def test_altSum():
    assert altSum([4, 3, 5, 2]) == 4
    assert altSum([2, 3, 5]) == 0
    assert altSum([5, 2]) == 7
    assert altSum([1]) == 1
    assert altSum([31, 4, 28, 5, 71]) == -59
    assert altSum([7, 7, 7, 7]) == 14
    assert altSum([]) == 0

