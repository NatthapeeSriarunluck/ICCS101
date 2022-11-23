class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Classroom:
    def __init__(self, students):
        self.students = students

    def find_average(self):
        total = 0
        amount = 0
        for student in self.students:
            total += student.score
            amount += 1
        return total / amount

    def find_median(self):
        sort = sorted(self.students)


Jack = Student('Jack', 90)
Ben = Student('Ben', 100)
Pat = Student('Pat', 80)
room = Classroom([Jack, Ben, Pat])
print(room.find_median())
