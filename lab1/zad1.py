
def mul(p):
    return [[(i*j)%p for i in range(p)] for j in range(p)]

def add(p):
    return [[(i+j)%p for i in range(p)] for j in range(p)]

def print_table(table, p, title):
    headers = [c for c in range(p)]
    
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
        
    print_divider(p+1)
        
def print_divider(column_count):
    print('_' * 4 * column_count, end='\n\n')

def show(p):
    print("Mnozenie")
    print_table(mul(p), p, '*')
    
    print("Dodawanie")
    print_table(add(p), p, '+')
    
[show(p) for p in [3, 5, 7]]