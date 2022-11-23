def total_damage(skill_book: dict[str, dict[str, int]], combat_log: list[tuple[str, str]]) -> int:
    ans = 0
    for hero, skill in combat_log:
        x = skill_book[hero]
        ans += x[skill]
    return ans


skill_book = {
    'mage': {'punch': 10, 'spellcast': 50},
    'shielder': {'punch': 5},
    'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}
}

assert total_damage(skill_book, [('mage', 'punch'), ('mage', 'punch')]) == 20  # each mage's punch deal 10 damage
assert total_damage(skill_book, [('mage', 'punch'), (
'vanguard', 'punch')]) == 30  # each vanguard's punch deal 20 damage, so the total is 10+20 = 30
assert total_damage(skill_book, [('mage', 'spellcast'), ('vanguard', 'punch'), ('vanguard', 'punch')]) == 90
assert total_damage(skill_book, [('vanguard', 'punch'), ('vanguard', 'kick'), ('shielder', 'punch')]) == 55
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast')]) == 1
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast')]) == 1
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'punch')]) == 10
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast')]) == 1
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast')]) == 1
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'spellcast'), ('healer', 'spellcast')]) == 51
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('shielder', 'punch'), ('shielder', 'punch')]) == 10
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'kick'), ('healer', 'spellcast')]) == 31
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'punch'), ('vanguard', 'punch')]) == 40
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast'), ('healer', 'spellcast')]) == 2
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'quickpunch'), ('shielder', 'punch'), ('shielder', 'punch'), ('vanguard', 'kick'),
                     ('shielder', 'punch')]) == 55
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'spellcast'), ('vanguard', 'quickpunch'), ('healer', 'spellcast'),
                     ('healer', 'spellcast'), ('shielder', 'punch')]) == 67
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast'), ('healer', 'spellcast'), ('mage', 'spellcast'), ('healer', 'spellcast'),
                     ('mage', 'punch')]) == 63
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'kick'), ('vanguard', 'quickpunch'), ('shielder', 'punch'), ('healer', 'spellcast'),
                     ('healer', 'spellcast')]) == 47
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'punch'), ('shielder', 'punch'), ('mage', 'punch'), ('mage', 'spellcast'),
                     ('healer', 'spellcast')]) == 76
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'kick'), ('mage', 'spellcast'), ('mage', 'punch'), ('shielder', 'punch'),
                     ('vanguard', 'kick'), ('shielder', 'punch'), ('mage', 'spellcast'), ('vanguard', 'punch'),
                     ('mage', 'spellcast'), ('mage', 'spellcast')]) == 300
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('vanguard', 'punch'), ('mage', 'punch'), ('mage', 'punch'), ('vanguard', 'punch'),
                     ('healer', 'spellcast'), ('vanguard', 'kick'), ('shielder', 'punch'), ('mage', 'spellcast'),
                     ('healer', 'spellcast'), ('mage', 'punch')]) == 157
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'punch'), ('vanguard', 'kick'), ('mage', 'punch'), ('vanguard', 'kick'),
                     ('vanguard', 'punch'), ('shielder', 'punch'), ('vanguard', 'kick'), ('healer', 'spellcast'),
                     ('shielder', 'punch'), ('mage', 'spellcast')]) == 191
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('healer', 'spellcast'), ('shielder', 'punch'), ('shielder', 'punch'), ('mage', 'spellcast'),
                     ('shielder', 'punch'), ('healer', 'spellcast'), ('shielder', 'punch'), ('mage', 'spellcast'),
                     ('healer', 'spellcast'), ('shielder', 'punch')]) == 128
assert total_damage({'mage': {'punch': 10, 'spellcast': 50}, 'shielder': {'punch': 5},
                     'vanguard': {'quickpunch': 10, 'punch': 20, 'kick': 30}, 'healer': {'spellcast': 1}},
                    [('mage', 'spellcast'), ('healer', 'spellcast'), ('healer', 'spellcast'), ('vanguard', 'kick'),
                     ('shielder', 'punch'), ('mage', 'spellcast'), ('shielder', 'punch'), ('mage', 'punch'),
                     ('shielder', 'punch'), ('vanguard', 'punch')]) == 177
