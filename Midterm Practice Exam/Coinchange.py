def coinChange(v: int) -> list[int]:
    value = v
    coins = []
    while value > 0:
        if value >= 10:
            coins.append(10)
            value -= 10
        elif value >= 5:
            coins.append(5)
            value -= 5
        elif value >= 2:
            coins.append(2)
            value -= 2
        elif value >= 1:
            coins.append(1)
            value -= 1
    return coins


'''
assert coinChange(38) == [10, 10, 10, 5, 2, 1]
assert coinChange(19) == [10, 5, 2, 2]
assert coinChange(11) == [10, 1]
assert coinChange(5) == [5]
assert coinChange(3) == [2, 1]
'''
