# Assignment 06, Task 03
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:20 hrs

def keepTabs(actions: list[str]) -> dict[str, int]:
    ans = make_dict(actions)
    for i in actions:
        if '++' in i:
            name, sign = i.split("++")
            ans[name] = ans[name] + 1
        if '--' in i:
            name, sign = i.split("--")
            ans[name] = ans[name] - 1
        if "->" in i:
            first, second = i.split("->")
            if first and second not in ans:
                continue
            new_value = ans[second] + ans[first]
            ans[second] = new_value
            ans[first] = ans[first] - ans[first]

    for i in list(ans.keys()):
        if ans[i] == 0:
            del ans[i]
    return ans


def make_dict(actions: list[str]) -> dict[str, int]:
    ans = {}
    for i in actions:
        if '++' in i:
            name, sign = i.split("++")
            ans[name] = 0
        if '--' in i:
            name, sign = i.split("--")
            ans[name] = 0
        if "->" in i:
            continue
    return ans



assert keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff",
                 "Jeff--", "June++", "Home->House"]) == {'Jeff': -2, 'June': 1, 'Jim': 2}
assert keepTabs(["JIm++", "Jim++", "Jim->JIm",]) == {"JIm": 2}
assert keepTabs(["JIm++", "Jim++", "Jim->JIm","JIM-> Jim"]) == {"JIm": 2}
assert keepTabs([""])== {}
assert keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff",
                 "Jeff--", "June++", "Home->House", "Jeff->John"]) == {'Jim':2,'John':-2,'June':1}


