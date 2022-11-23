vowels = 'aeiouAEIOU'
lower = 'bcdfghjklmnpqrstvwxyz'
upper = 'BCDFGHJKLMNPQRSTVWXYZ'


def better_swap_case(st: str) -> str:
    new = ""
    for x in st:
        if x in vowels:
            new += x
        elif x in lower:
            new += x.upper()
        elif x in upper:
            new += x.lower()
        else:
            new += " "
    return new


'''
assert better_swap_case('WbS') == 'wBs'
assert better_swap_case('XUOfuN') == 'xUOFun'
assert better_swap_case('OpFuod') == 'OPfuoD'
assert better_swap_case('pGHa') == 'Pgha'
assert better_swap_case('uMHruZY7') == 'umhRuzy '
assert better_swap_case('EkbrEO:=l') == 'EKBREO  L'
assert better_swap_case('I)oQ0ZLCJ') == 'I oq zlcj'
assert better_swap_case('iO5^uia') == 'iO  uia'
assert better_swap_case('v6q`uiI2') == 'V Q uiI '
assert better_swap_case('E2;RoF~3') == 'E  rof  '

'''
