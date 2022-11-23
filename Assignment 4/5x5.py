def border_sum(M):
    total = 0
    for i in range(5):
        for j in range(5):
            if  i == 0 or i == 4:
                total += M[j]