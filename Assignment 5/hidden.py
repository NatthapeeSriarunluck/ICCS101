# Assignment 05, Task 02
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:30 hrs

def is_hidden(s: str, t: str) -> bool:
    hidden = t.lower()
    main = s.lower()
    j = 0
    compare = ''
    for i in range(len(hidden)):
        while j < len(main):
            if main[j] == hidden[i]:
                compare += hidden[i]
                j += 1
                break
            else:
                j += 1
                continue
    if compare == hidden:
        return True
    else:
        return False
