def winner(records: list[dict[str,int]]) -> str:
    lst = [max(i, key=i.get) for i in records]
    dic = {}
    for i in lst:
        dic[i] = dic.get(i, 0) + 1
    max_value = 0
    ans = ''
    for key,value in dic.items():
        if value > max_value:
            max_value = value
    for key,value in dic.items():
        if value == max_value:
            ans+= key
    if len(ans) > 1:
        return ''
    else:
        return ans


assert winner([{'A':2,'B':1}]) == 'A'
assert winner([{'A':3,'B':0},{'A':1,'C':2}]) == ''
assert winner([{'A':3,'B':0},{'A':1,'C':2},{'B':0,'C':3}]) == 'C'
assert winner([{'A':3,'B':0},{'A':1,'C':2},{'B':0,'D':3},{'A':2,'D':1}]) == 'A'
assert winner([{'A':3,'B':0},{'B':2,'C':1},{'C':2,'D':1},{'A':0,'D':3}]) == ''