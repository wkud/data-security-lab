def show(p):
    values = []
    for i in range(1, p):
        x = 0
        while (x * i)%p != 1:
            x += 1
        values.append(x)
            
    print(values)

[show(i) for i in [3, 5, 7]]
