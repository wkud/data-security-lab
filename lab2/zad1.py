
def mul(q):
    return [[mul_value(i, j, q) for i in range(-1, q-1)] for j in range(-1, q-1)]

def to_power_of_a(x):
    if x-1 == -1:
        return "0 "
    if x-1 == 0:
        return "1 "
    return f'a{x-1}'

def mul_value(i, j, q):
    n = (i+j)%(q-1)
    if i == -1 or j == -1:
        return -1
    if n == 0:
        return 0
    return n

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
                col_as_a = to_power_of_a(col+1)
                print(col_as_a, end=' | ')
            else:
                print(col+1, end=' | ')
        print()
        i += 1
        
    print_divider(q+1)
        
def print_divider(column_count):
    print('_' * 4 * column_count, end='\n\n')

def show(q, is_a):
    print("Mnozenie")
    print_table(mul(q), q, '* ', is_a)
    
if __name__ == "__main__":
    [show(q) for q in [8, 16]]