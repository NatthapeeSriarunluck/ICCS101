class Duration:
    def __init__(self, hour: int, minute: int, second: int):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        if self.minute > 60 or self.second > 60:
            raise ValueError("minute or second can't be more than 60")
        return f'{self.hour} hour {self.minute} min {self.second} sec'

    def __repr__(self):
        return f'{self.hour} hour {self.minute} min {self.second} sec'

    def __add__(self, other):
        total_sec = self.second + other.second
        total_min = self.minute + other.minute
        total_hour = self.hour + self.hour
        if total_sec >= 60:
            total_sec -= 60
            total_min += 1
        if total_min >= 60:
            total_min -= 60
            total_hour += 1
        return f'{total_hour} hour {total_min} minute {total_sec} sec'

    def


dur = Duration(1, 51, 54)
print(dur)
a = Duration(0, 10, 10)
b = Duration(0, 50, 50)
a += b
print(a)
