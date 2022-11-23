# Assignment 05, Task 6
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 07:00 hrs

def separate(data: list[int], k) -> list[list[int]]:
    if k == 1:
        return [data]
    all_gaps = []
    cycle = k - 1
    ans = []
    for i in range(len(data) - 1):
        all_gaps.append(data[i + 1] - data[i])
    split_index = []
    while cycle > 0:
        copy = data[:]
        for i in range(len(copy) - 1):
            if abs(copy[i] - copy[i + 1]) == max(all_gaps):
                split_index.append(i)
                all_gaps.remove(max(all_gaps))
                cycle -= 1
                break
    sorted_index = sorted(split_index)
    tmp_index = 0
    for i in sorted_index:
        ans.append(data[tmp_index: i + 1])
        tmp_index = i + 1
    ans.append(data[tmp_index:])
    return ans
