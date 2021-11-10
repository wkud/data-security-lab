
def mul(q):
    return [[mul_value(i, j, q) for i in range(-1, q-1)] for j in range(-1, q-1)]

def mul_value(i, j, q):
    n = (i+j)%(q-1)
    if i == -1 or j == -1:
        return "0 "
    if n == 0:
        return "1 "
    return f'a{n}'

def print_table(table, q, title):
    headers = [f'a{c}' for c in range(-1, q-1)]
    for i in range(len(headers)):
        header = headers[i]
        if header == "a-1":
            headers[i] = "0 "
        
    print(title, end=' | ')
    
    for col_header in headers:
        
        print(col_header, end=' | ')
    print()
    
    i = 0
    for row in table:
        print(headers[i], end=' | ') 
        for col in row:
            print(col, end=' | ')
        print()
        i += 1
        
    print_divider(q+1)
        
def print_divider(column_count):
    print('_' * 4 * column_count, end='\n\n')

def show(q):
    print("Mnozenie")
    print_table(mul(q), q, '* ')
    
[show(q) for q in [8, 16]]