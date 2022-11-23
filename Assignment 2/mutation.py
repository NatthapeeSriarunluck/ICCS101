# Assignment 02, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 6:00 hrs

s: str = "dFJSJDkk"
t: str = "dflkTkdf"
s123 = s.lower().replace('s', 'm').replace('l', 'm').replace('a', 'm')
t123 = t.upper().replace('P', 'T').replace('O', 'T').replace('I', 'T').replace('N', 'T')
first_character_of_s123 = s123[0]
first_character_of_t123 = t123[0]
s4 = first_character_of_t123 + (s123[1:])
t4 = first_character_of_s123 + (t123[1:])
ks = len(s) // 3
kt = len(t) // 3
last_third_cha_of_s4 = s4[ks * 2:]
middle_third_cha_of_t4 = t4[kt: 2 * kt]
s5 = s4.replace(last_third_cha_of_s4, middle_third_cha_of_t4)
z = s5 + t4
print(z)