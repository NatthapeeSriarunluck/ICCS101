# Assignment 07, Task 02
# Name: Natthapee Sriarunluck
# Collaborators: Achira Laovong
# Time Spent: 10:00 hrs

Hand = set[tuple[str, str]]

Value = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13,
         'A': 14}
Suit = ['Diamond', 'Heart', 'Club', 'Spades']
Rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
all_cards = [(i, j) for i in Suit for j in Rank]


def is_straight_flush(h: Hand) -> bool:
    suit = [i[0] for i in h]
    rank = sorted([Value[i[1]] for i in h])
    if suit[0] == suit[1] == suit[2] == suit[3] == suit[4]:
        if rank[0] == 2 and rank[3] == 5 and rank[4] == 14:
            low_ace = [1] + rank
            low_ace.remove(14)
            return low_ace[-1] - low_ace[0] == 4
        return rank[-1] - rank[0] == 4
    return False


def is_four_of_a_kind(h: Hand) -> bool:
    card = [(j, i) for i, j in h]
    sort_card = sorted(card)
    return sort_card[0][0] == sort_card[3][0] or sort_card[1][0] == sort_card[4][0]


def is_full_house(h: Hand) -> bool:
    dic = {}
    for k, v in h:
        if v not in dic:
            dic[v] = [k]
        else:
            dic[v].append(k)
    list_key = list(dic.keys())
    for i in list_key:
        if len(dic[i]) == 3 or len(dic[i]) == 2:
            continue
        return False
    return True


def is_two_pair(h: Hand) -> bool:
    dic = {}
    for k, v in h:
        if v not in dic:
            dic[v] = [k]
        else:
            dic[v].append(k)
    list_key = list(dic.keys())
    if len(list_key) == 3:
        for i in list_key:
            if len(dic[i]) == 2 or len(dic[i]) == 1:
                continue
            return False
        return True
    return False


def all_hands():
    combo = combinations(all_cards, 5)
    return [set(i) for i in combo]


def combinations(lst, amount):
    if amount == 0:
        return [[]]
    if len(lst) == amount:
        return [list(lst)]
    ans = [[lst[0]] + i for i in combinations(lst[1:], amount - 1)]
    ans += combinations(lst[1:], amount)
    return ans


def all_straight_flush() -> list[Hand]:
    return [hand for hand in all_hands() if is_straight_flush(hand)]


def all_four_of_a_kind() -> list[Hand]:
    return [hand for hand in all_hands() if is_four_of_a_kind(hand)]


def all_full_house() -> list[Hand]:
    return [hand for hand in all_hands() if is_full_house(hand)]


def all_two_pair() -> list[Hand]:
    return [hand for hand in all_hands() if is_two_pair(hand)]
