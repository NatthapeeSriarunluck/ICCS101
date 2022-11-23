def processOrders(orders: list[int], sizes: list[int]) -> list[bool]:
    ans = []
    all_lengths = []
    for i in range(len(sizes)):
        for j in range(len(sizes)):
            all_lengths.append(sizes[i])
            all_lengths.append(sizes[i] + sizes[j])
    for order in orders:
        if order in all_lengths:
            ans.append(True)
        else:
            ans.append(False)
    return ans


assert (processOrders([5, 7, 13], [3, 5, 6, 10]) == [True, False, True])
assert (processOrders([5, 12, 13, 20], [1, 2, 5, 10])
        == [True, True, False, True])
assert (processOrders([9, 116, 169], [20, 23, 32, 36])
        == [False, False, False])
assert (processOrders([9, 13, 39, 128, 184, 187], [
        13, 15, 19, 20, 22, 27, 33, 40, 43, 45]) == [False, True, True, False, False, False])
assert (processOrders([28, 29, 60, 88, 117, 133, 140, 144, 160], [3, 5, 7, 11, 14, 16, 20, 22,
                                                                  24, 26, 32, 34, 42, 43]) == [True, True, True, False, False, False, False, False, False])
assert (processOrders([4, 7, 16, 21, 43, 64, 77, 83, 106, 116, 165, 182], [6, 8, 10, 14, 18, 20, 25, 27, 33, 34,
                                                                           36, 37, 43, 44, 47, 48, 49]) == [False, False, True, False, True, True, True, True, False, False, False, False])
assert (processOrders([17, 21, 63, 68, 77, 83, 84, 92, 114, 134, 151, 162, 163, 165, 184], [1, 2, 4, 6, 8, 10, 11, 13, 16, 19, 20, 21, 23,
                                                                                            26, 28, 29, 38, 39, 40, 41, 45]) == [True, True, True, True, True, True, True, False, False, False, False, False, False, False, False])
