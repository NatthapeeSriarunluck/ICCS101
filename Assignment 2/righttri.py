# Assignment 02, Task 07
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent:00:15 hrs

x: float
y: float
z: float = 3.0
c = max(x, y, z)
s = c ** 2
r = x ** 2 + y ** 2 + z ** 2 - s
right_triangle: bool = (abs(s - r) < 1e-7)

