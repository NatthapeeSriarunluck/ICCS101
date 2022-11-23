ans1 = []
for i in range(1, 11):
    ans1.append(i + 13)
print(ans1)
print([number + 13 for number in range(1, 11)])

ans2 = []
for i in range(1, 10):
    if i % 2 == 0:
        ans2.append("even")
    else:
        ans2.append("odd")
print(ans2)
print([("odd", "even")[i % 2 == 0] for i in range(1, 10)])

ans3 = []
for i in range(1, 10):
    for j in range(1, 10):
        if i != j:
            ans3.append((i, j))
print(ans3)
print([(i, j) for i in range(1, 10) for j in range(1, 10) if i != j])
