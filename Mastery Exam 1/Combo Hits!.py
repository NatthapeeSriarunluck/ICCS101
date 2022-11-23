def total_damage(actions_list: list[str]) -> int:
    damage = 0
    n = 0
    if len(actions_list) == 0:
        return 0
    if len(actions_list) < 3:
        for x in actions_list:
            if x == 'Q':
                damage += 10
            else:
                damage += 7
        return damage
    while n + 2 < len(actions_list):
        if actions_list[n] == 'Q':
            if actions_list[n + 1] == 'Q':
                if actions_list[n + 2] == 'E':
                    damage += 47
                    n += 3
                    continue
            damage += 10
            n += 1
        else:
            damage += 7
            n += 1
    if n < len(actions_list):
        if actions_list[n] == 'Q':
            damage += 10
            n += 1
        else:
            damage += 7
            n += 1
    if n < len(actions_list):
        if actions_list[n] == 'Q':
            damage += 10
            n += 1
        else:
            damage += 7
            n += 1
    return damage

assert (total_damage([]) == 0)
assert (total_damage(['Q']) == 10)
assert (total_damage(['E']) == 7)
assert (total_damage(['Q', 'Q']) == 20)
assert (total_damage(['Q', 'Q', 'E']) == 47)
assert (total_damage(['Q', 'Q', 'Q', 'E']) == 57)
assert (total_damage(['Q', 'Q', 'Q', 'E', 'E']) == 64)
assert (total_damage(['Q', 'Q', 'E', 'Q', 'Q', 'Q']) == 77)
assert (total_damage(['Q', 'Q', 'E', 'Q', 'Q', 'E']) == 94)
assert (total_damage(['Q', 'Q', 'Q', 'Q', 'E', 'Q', 'Q', 'E']) == 114)
assert (total_damage(['Q', 'Q', 'Q', 'Q', 'E', 'Q', 'Q', 'E', 'Q', 'E', 'E']) == 138)
assert (total_damage(['Q', 'E', 'Q', 'Q', 'Q']) == 47)
assert (total_damage(['E', 'Q', 'Q', 'E', 'Q', 'Q', 'E']) == 101)
assert (total_damage(['E', 'Q', 'E', 'Q', 'Q', 'Q', 'Q', 'E', 'Q']) == 101)
assert (total_damage(['Q', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'Q', 'E']) == 83)
assert (total_damage(['E', 'Q', 'Q', 'Q', 'E', 'Q', 'E', 'Q', 'E', 'E', 'E', 'E', 'Q']) == 129)
assert (total_damage(['E', 'E', 'E', 'E', 'E', 'E', 'E', 'E', 'Q', 'Q', 'E', 'E', 'Q', 'Q', 'Q']) == 140)
assert (total_damage(['Q', 'Q', 'E', 'E', 'Q', 'E', 'E', 'E', 'Q', 'Q', 'E', 'E', 'Q', 'E', 'Q', 'Q', 'Q']) == 186)
assert (total_damage(
    ['E', 'E', 'Q', 'E', 'Q', 'E', 'E', 'E', 'Q', 'Q', 'E', 'E', 'Q', 'E', 'E', 'Q', 'E', 'E', 'Q']) == 174)
