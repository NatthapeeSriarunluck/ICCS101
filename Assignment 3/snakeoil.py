# Assignment 03, Task 02
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:30 hrs

def price(vol: int) -> float:
    if vol < 20:
        return float(vol * 18 + 250)
    if 20 <= vol <= 100:
        return float(vol * 18 + vol * 10)
    if vol > 100:
        return vol * 18 * 0.99

