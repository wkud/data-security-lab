def show(p):
    values = []
    for i in range(2, p):
        n = 1
        group = []
        repetition = 0
        while repetition == 0: # or repetition < len(group):
            v = (i**n)%p
            if(v not in group):
                group.append(v)
            else:
                repetition += 1
            n += 1
                
        if len(group) == p-1: # jezeli i tworzy grupę multiplikatywną
            values.append(i)
    print(values)
        

[show(p) for p in [3, 5, 7]]