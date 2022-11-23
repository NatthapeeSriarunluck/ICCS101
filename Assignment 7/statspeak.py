# Assignment 07, Task 03
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:00 hrs


class DataFrame:
    def __init__(self,):
        self.items: list[float] = []

    def add(self, x):
        if isinstance(x, int):
            self.items = self.items + [x]
            return self.items
        elif isinstance(x, list):
            for i in x:
                self.items += [i]
            return self.items
        elif isinstance(x, tuple):
            for i in x:
                self.items += [i]
            return self.items

    def mean(self):
        total = 0
        for i in self.items:
            total += i
        return total / len(self.items)

    def percentile(self, r):
        if r > 99 or r < 0:
            raise ValueError("r can't be less than 0 or bigger than 99")
        return sorted(self.items)[int(r / 100 * len(self.items))]

    def mode(self):
        dic = {}
        for i in self.items:
            dic[i] = dic.get(i, 0) + 1
        return max(dic, key=dic.get)

    def sd(self):
        lst = [(i - self.mean()) ** 2 for i in self.items]
        total = 0
        for i in lst:
            total += i
        return (total / (len(lst) - 1)) ** (1 / 2)

    def __repr__(self):
        return f'{self.items}'


print(DataFrame(1))
