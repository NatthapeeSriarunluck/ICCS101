def is_dead(L: list[int], init_hp: int) -> bool:
    health = init_hp
    if health == 0:
        return True
    for x in L:
        health += int(x)
        if health > 0:
            continue
        elif health < 0:
            return True
        else:
            return True
    if health > 0:
        return False


assert (is_dead([-10], 1) == True)
assert (is_dead([10, -10], 1) == False)
assert (is_dead([10, 10, 10], 0) == True)
assert (is_dead([10, -20, 1000], 1) == True)
assert (is_dead([43, -103, 95, 57, 16, -143], 99) == False)
assert (is_dead([-2, 32, 100, 83, -221, 58], 8) == True)
assert (is_dead([27, 19, -33, 17, 31, -22, 56, 59], 13) == False)
assert (is_dead([-40, 2, -10, 41, -10, -12, 87, -34], 48) == True)
assert (is_dead([26, 22, -35, 43, 69, 77, -200, 73, 94, 86], 53) == False)
assert (is_dead([-51, 59, -16, -47, 46, -56, 54, 58, 97, 69], 60) == True)
assert (is_dead([89, -144, 25, 76, 65, 23, -69, -96, 81, -65, 3, 17], 80) == False)
assert (is_dead([-19, -16, 45, 64, 22, -93, -93, 47, 7, 94, -38, 42], 100) == False)
assert (is_dead([0], 1)) == False
assert (is_dead([1], 0)) == True
