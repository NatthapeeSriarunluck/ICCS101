# Assignment 05, Task 04
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 01:30 hrs
def jogging_average(activities: list[str]) -> float:  # main
    log = activities[:]
    total_distance = 0
    total_time = 0
    for i in range(len(log)):
        j = 0
        while j < len(log[i]):
            if log[i][j: j + 7] == 'jogging':
                total_distance += parse_dist(log[i])
                total_time += parse_time(log[i])
                break
            else:
                break
    return total_distance * 1000 / total_time


def parse_time(line: str) -> int:
    time = ''
    i = 13
    while i < len(line):
        if line[i] != ';':
            time += line[i]
            i += 1
        else:
            break
    minutes, second = time.split(',')
    return 60 * int(minutes) + int(second)


def parse_dist(line: str) -> float:
    x = line
    y = str(x.split(':', 1)[1])
    z = str(y.split(':', 1)[1])
    return float(z)


assert jogging_average(["jogging;time:364,00;distance:1.3",
                        "jogging;time:16,00;distance:3.3",
                        "jogging;time:36,05;distance:553.54",
                        "jojging;time:30,20;distance:544.383742",
                        "jogging;time:566,25;distance:642.398724",
                        "jogging;time:326,45;distance:9912.3",
                        "jogging;time:35,65;distance:0.3", ]) - 137.67515763131814 < 0.0001
