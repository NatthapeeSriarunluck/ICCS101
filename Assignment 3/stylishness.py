# Assignment 03, Task 07
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:00 hrs

def got_table(you: int, date: int) -> str:
    if (you <= 2) or (date <= 2):
        return "no"
    elif ((you >= 8) or (date >= 8)) and ((you > 2) and (date > 2)):
        return "yes"
    else:
        return "maybe"


print(got_table(1,10))
