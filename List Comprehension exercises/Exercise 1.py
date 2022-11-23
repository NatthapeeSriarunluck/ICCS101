def mult_ten(n: int) -> list[int]:
    return [i * 10 for i in range(1, n + 1)]


def cubes(n: int) -> list[int]:
    return [i ** 3 for i in range(1, n + 1)]


def awesome(names: list[str]) -> list[str]:
    return [f'{i} is awesome!' for i in names]


def to_lower(words: list[str]) -> list[str]:
    return [i.lower() for i in words]


def filter_vowels(words: list[str]) -> list[str]:
    set_vowels = {'a', 'e', 'i', 'o', 'u'}
    return [word for word in words if len(set_vowels & set(word)) == 0]


def dict_sum(data: dict[str:int]) -> list[int]:
    return [dic['v1'] + dic['v2'] for dic in data]


assert mult_ten(5) == [10, 20, 30, 40, 50]
assert cubes(3) == [1, 8, 27]
assert awesome(['John', 'Mark']) == ['John is awesome!', 'Mark is awesome!']
assert to_lower(['Hello', 'WoRlD']) == ['hello', 'world']
assert filter_vowels(['Hello', 'NVM', 'brb', 'lol']) == ['NVM', 'brb']
assert dict_sum([{'v1': 1, 'v2': 10}, {'v1': 2, 'v2': 20}, {'v1': 3, 'v2': 30}]) == [11, 22, 33]
