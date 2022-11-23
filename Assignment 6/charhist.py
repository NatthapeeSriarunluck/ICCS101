# Assignment 06, Task 01
# Name: Natthapee Sriarunluck
# Collaborators: -
# Time Spent: 10:00 hrs

alphabet = 'abcdefghijklmnopqrstuvwxyz'


def charHistogram(filename: str) -> None:
    frequency = {}
    with open(filename, 'r') as files:
        for lines in files:
            for letters in lines.lower():
                if letters in alphabet:
                    frequency[letters] = frequency.get(letters, 0) + 1
                elif letters == '\n' or letters == ' ' or letters == '\r' or letters == '\t' or letters == '.' or letters == ',':
                    continue
                else:
                    continue
    list_sorted_values = sorted(list(frequency.values()), reverse=True)
    list_keys = list(frequency.keys())
    sorted_frequency = {}
    for i in list_sorted_values:
        for j in list_keys:
            if frequency[j] == i:
                sorted_frequency[j] = i
    group_alphabet = sort_alphabet(sorted_frequency)
    sorted_group_alphabet = []
    for i in range(len(group_alphabet)):
        if len(group_alphabet[i]) > 1:
            sorted_group_alphabet.append(sorted(group_alphabet[i]))
        else:
            sorted_group_alphabet.append(group_alphabet[i])
    flat_sorted_group_alphabet = []
    for i in range(len(sorted_group_alphabet)):
        for j in range(len(sorted_group_alphabet[i])):
            flat_sorted_group_alphabet.append(sorted_group_alphabet[i][j])
    final_dict = dict(zip(flat_sorted_group_alphabet, list_sorted_values))
    final_key = list(final_dict.keys())
    for i in range(len(final_key)):
        print(f'{final_key[i]} {"+" * final_dict[final_key[i]]}')
    files.close()


def sort_alphabet(dic: dict[str, int]) -> list:
    flipped = {}
    for key, value in dic.items():
        if value not in flipped:
            flipped[value] = [key]
        else:
            flipped[value].append(key)
    return list(flipped.values())


