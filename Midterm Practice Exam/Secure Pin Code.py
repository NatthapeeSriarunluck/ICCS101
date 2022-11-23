def pincode(k: int) -> int:
    total = 0
    count = 0
    for pin in range(10000):
        for x in str(pin):
            total += int(x)
        if total % k == 0:
            total = 0
            count += 1
        else:
            total = 0
            continue
    return count


assert pincode(35) == 5
assert pincode(36) == 2
assert pincode(20) == 634
assert pincode(49) == 1
