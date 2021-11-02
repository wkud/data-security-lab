def show(p):
    values = []
    for i in range(1, p):
        n=1
        while (i**n)%p != 1:
            n += 1
        values.append(n)
    print(values)

[show(p) for p in [3, 5, 7]]