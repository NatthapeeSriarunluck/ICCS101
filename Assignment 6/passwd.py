# Assignment 06, Task 02
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:30 hrs

upper_character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_character = 'abcdefghijklmnopqrstuvwxyz'
digit = '0123456789'
special = '$#@%!'


def passwordOK(password: str) -> bool:
    upper = 0
    lower = 0
    dig = 0
    spe = 0
    if not repetitive(password) and 6 <= len(password) <= 12:
        for i in password:
            if i in upper_character:
                upper += 1
            if i in lower_character:
                lower += 1
            if i in digit:
                dig += 1
            if i in special:
                spe += 1
        if upper == 0 or lower == 0 or dig == 0 or spe == 0:
            return False
        return True
    return False


def repetitive(n: str) -> bool:
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] == n[i + 2]:
            return True
    return False


assert passwordOK('ABd1234@1') == True
assert passwordOK('ABD1234@1') == False
assert passwordOK('abd1234@1') == False
assert passwordOK('ABd123411') == False
assert passwordOK('a1A#') == False
assert passwordOK('ABd1234@1abcd') == False
assert passwordOK('ABd1234@1AAA') == False
assert passwordOK('ABd1234@1222') == False
assert passwordOK('a') == False
assert passwordOK('AAAd1234@1ab1') == False
assert passwordOK('111234@1AAA') == False