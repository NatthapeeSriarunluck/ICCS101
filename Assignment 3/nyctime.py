# Assignment 03, Task 06
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:00 hrs

def nycHour(bkkHour: int) -> str:
    if bkkHour < 10:
        return str(bkkHour + 1) + 'pm'
    if 23 > bkkHour > 11:
        return str(bkkHour - 11) + 'am'
    if bkkHour == 11:
        return str(12) + 'am'
    if bkkHour == 23:
        return str(12) + 'pm'

