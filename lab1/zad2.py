def show(p):
    values = [(0-i)%p for i in range(p)]
    print(values)
    
[show(p) for p in [3, 5, 7]]