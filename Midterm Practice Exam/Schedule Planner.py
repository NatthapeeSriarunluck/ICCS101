def create_schedule(nap_slots: list[int], engagements: list[str]) -> list[str]:
    schedule: list[str] = engagements[:]
    for i in nap_slots:
        schedule.insert(i, '*Nap*')
    return schedule

assert create_schedule([2], ['ntwagqckdz', 'nhyt', 'njtj']) == ['ntwagqckdz', 'nhyt', '*Nap*', 'njtj']
assert create_schedule([0, 5], ['yyhuthqp', 'nkqfemfp', 'agwgbyi', 'nzpwz']) == ['*Nap*', 'yyhuthqp', 'nkqfemfp', 'agwgbyi', 'nzpwz', '*Nap*']
assert create_schedule([1, 2, 4], ['dsbjc', 'vmeegjvin', 'ljaqslgk', 'wvfzelpn']) == ['dsbjc', '*Nap*', '*Nap*', 'vmeegjvin', '*Nap*', 'ljaqslgk', 'wvfzelpn']
assert create_schedule([4, 6, 7], ['rzkctkp', 'zknrlruky', 'ufgtzlj', 'pnjrn', 'eypsqoh', 'gdhn']) == ['rzkctkp', 'zknrlruky', 'ufgtzlj', 'pnjrn', '*Nap*', 'eypsqoh', '*Nap*', '*Nap*', 'gdhn']
assert create_schedule([0, 3, 5], ['ngsocqwq', 'hbckg', 'uyjaaoey', 'hnuv', 'hdkitjfeji', 'jndm', 'stknijqo', 'smiuoylv', 'ljnjxii', 'kwvizqjxg']) == ['*Nap*', 'ngsocqwq', 'hbckg', '*Nap*', 'uyjaaoey', '*Nap*', 'hnuv', 'hdkitjfeji', 'jndm', 'stknijqo', 'smiuoylv', 'ljnjxii', 'kwvizqjxg']
assert create_schedule([1, 2, 12, 13, 17], ['kzmq', 'cfkm', 'lokykqhb', 'akukxnfar', 'eidvhiqny', 'ojljoz', 'tjuq', 'cmokfhhnaz', 'ewrlbbjkx', 'ioceeruega', 'okfrigyc', 'gyzksmje', 'intgpu', 'miicmppoih', 'bnkkafq', 'luahw', 'tccwogtmn', 'thbl', 'dzyegcwy', 'iruhhd']) == ['kzmq', '*Nap*', '*Nap*', 'cfkm', 'lokykqhb', 'akukxnfar', 'eidvhiqny', 'ojljoz', 'tjuq', 'cmokfhhnaz', 'ewrlbbjkx', 'ioceeruega', '*Nap*', '*Nap*', 'okfrigyc', 'gyzksmje', 'intgpu', '*Nap*', 'miicmppoih', 'bnkkafq', 'luahw', 'tccwogtmn', 'thbl', 'dzyegcwy', 'iruhhd']