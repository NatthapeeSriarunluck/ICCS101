def best_shopping_plan(prices: list[int], amount: int) -> int:
    if amount <= 0:
        return 0
    if prices == []:
        return 0
    lst = sorted(prices)
    all_price = []
    for i in range(len(lst)):
        all_price.append(lst[i])
        j = i + 1
        while j < len(lst):
            all_price.append(lst[i] + lst[j])
            j += 1
    sorted_all_price = list(set(sorted(all_price)))
    for i in sorted_all_price:
        if i == amount:
            return i
    for i in range(len(sorted_all_price) - 1, -1, -1):
        if sorted_all_price[i] < amount:
            return sorted_all_price[i]
    return 0


assert best_shopping_plan([], 1) == 0  # Alice cannot buy anything as there is no item in the store
assert best_shopping_plan([1], 1) == 1  # Alice can only buy that one item of price 1 given her budget amount
assert best_shopping_plan([1, 2], 1) == 1  # Alice can only buy that one item of price 1 given her budget amount
assert best_shopping_plan([1, 1, 2],
                          2) == 2  # Alice can buy one item of price 2, or she can buy the two items of price 1
assert best_shopping_plan([1, 2, 3],
                          3) == 3  # Alice can buy one item of price 3, or she can buy the two items of price 1 and 2
assert best_shopping_plan([1, 2, 3, 4], 10) == 7  # The best Alice can buy is for items of prices 3 and 4
assert best_shopping_plan([1, 2, 2, 3, 3, 3], 10) == 6  # The best Alice can buy is for items of prices 3 and 3
assert best_shopping_plan([1, 1, 1, 3, 5, 5], 7) == 6  # The best Alice can buy is for items of prices 1 and 5
assert best_shopping_plan([29, 13, 18], 15) == 13
assert best_shopping_plan([29, 13, 18], 16) == 13
assert best_shopping_plan([29, 13, 18], 33) == 31
assert best_shopping_plan([21, 27, 45, 36, 37], 27) == 27
assert best_shopping_plan([21, 27, 45, 36, 37], 63) == 63
assert best_shopping_plan([21, 27, 45, 36, 37], 29) == 27
assert best_shopping_plan([43, 7, 12, 27, 1, 44, 50], 20) == 19
assert best_shopping_plan([43, 7, 12, 27, 1, 44, 50], 18) == 13
assert best_shopping_plan([43, 7, 12, 27, 1, 44, 50], 51) == 51
assert best_shopping_plan([30, 44, 5, 46, 50, 50, 37, 6, 9], 9) == 9
assert best_shopping_plan([30, 44, 5, 46, 50, 50, 37, 6, 9], 30) == 30
assert best_shopping_plan([30, 44, 5, 46, 50, 50, 37, 6, 9], 33) == 30
assert best_shopping_plan([30, 44, 5, 46, 50, 50, 37, 6, 9], 0) == 0
assert best_shopping_plan([30, 44, 5, 46, 50, 50, 37, 6, 9], -1 ) == 0
assert best_shopping_plan([2], 1) == 0
assert best_shopping_plan([1, 1, 1, 1], 30) == 2
assert best_shopping_plan([30, 30, 30, 30], 1) == 0
assert best_shopping_plan([30], 1) == 0
assert best_shopping_plan([30], 30) == 30