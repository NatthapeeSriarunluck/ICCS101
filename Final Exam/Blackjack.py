rank = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10 ': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 1}


class BlackJackHand:
    def __init__(self, ):
        self.cards: list[str] = []

    def value(self):
        value = 0
        for i in self.cards:
            value += rank[i]
        if 'A' in self.cards:
            if value <= 11:
                value += 10
        return value

    def draw(self, card: str):
        if self.value() >= 17:
            return self.cards
        elif len(card) > 1:
            return self.cards
        else:
            return self.cards.append(card)

    def is_bust(self) -> bool:
        if self.value() > 21:
            return True
        return False

    def __repr__(self):
        return f'{[i for i in self.cards]}'


h1 = BlackJackHand()
h1.draw('A')
h1.draw('5')
assert h1.cards == ['A', '5']
assert h1.value() == 16  # 'A' is 11 and '5' is 5, so 11+5 = 16
h1.draw('3')
assert h1.cards == ['A', '5', '3']
assert h1.value() == 19
h1.draw('2')  # can not add card '2' as the current hand value is 19 (note: 19>16)
assert h1.cards == ['A', '5', '3']
assert h1.is_bust() == False

h2 = BlackJackHand()
h2.draw('K')
h2.draw('5')
assert h2.cards == ['K', '5']
assert h2.value() == 15
h2.draw('A')
assert h2.value() == 16  # last 'A' was added as 1, because otherwise 15+11>21
assert h2.cards == ['K', '5', 'A']
h2.draw('abc')  # invalid card string, no card is added
assert h2.cards == ['K', '5', 'A']
h2.draw('9')  # can still add card '9' as the current hand value is still 16
assert h2.cards == ['K', '5', 'A', '9']
assert h2.value() == 25
assert h2.is_bust() == True  # the hand value is more than 21
h3 = BlackJackHand()
h3.draw('K')