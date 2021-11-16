from zad1 import show as show_mult

Z = {4: [2,1],
    8: [3, 6, 1, 5, 4, 2],
    16: [4, 8, 14, 1, 10, 13, 9, 2, 7, 5, 12, 11, 6, 3],
    32: [20, 9, 26, 18, 8, 21, 29, 5, 2, 16, 12, 11, 17, 27, 25, 10, 13, 4, 30, 1, 6, 24, 28, 22, 15, 3, 14, 23, 7, 19]}


def add(q):
    return [[add_value(i, j, q) for i in range(0, q)] for j in range(0, q)]

def add_value(x, y, q):
    if (x != 0 and y == x):
        return 0
    
    if (x == 0 or y == 0):
        return x + y
    
    _x = max(x, y)
    _y = min(x, y)
    i = _x-_y-1
    return (_y + Z[q][i] -1) % (q-1) + 1
    
    
def to_power_of_a(x):
    if x-1 == -1:
        return "0 "
    if x-1 == 0:
        return "1 "
    return f'a{x-1}'

def print_table(table, q, title, is_a):
    headers = [c for c in range(0, q)]
    
    if(is_a):
        for i in range(len(headers)):
            headers[i] = to_power_of_a(headers[i])
        
    print(title, end=' | ')
    
    for col_header in headers:
        print(col_header, end=' | ')
    print()
    
    i = 0
    for row in table:
        print(headers[i], end=' | ') 
        for col in row:
            if is_a:
                col_as_a = to_power_of_a(col)
                print(col_as_a, end=' | ')
            else:
                print(col, end=' | ')
        print()
        i += 1
        
    print_divider(q+1)
        
def print_divider(column_count):
    print('_' * 4 * column_count, end='\n\n')

def show(q, is_a):
    print("Dodawanie")
    print_table(add(q), q, '+ ', is_a)

q_input = [4, 8, 16]
is_a = False
    
[(show(q, is_a), show_mult(q, is_a)) for q in q_input]


