# Assignment 1, Task 6
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 00:30 hrs

### DO NOT REMOVE THIS PART ###

# Update this variable to the last three digits
# of your student id *WITHOUT* leading 0's.
last_three: int = 266

# a=266th digit of magic number from left
# b=266th digit of magic number from right
M = str(832323811 ** (18323 + 2381) + 381818183 ** (18183 - 3818))
a = M[last_three-1]
b = M[-last_three]
print(f'My secret code is {b}{a}')
