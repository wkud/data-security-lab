polynomial = [1, 0, 1, 1]
start_sequence = [1, 0, 0]
p=2

def get_next(sequence, complement):    
    return sum([complement[index] * sequence[-(index+1)] for index in range(len(complement))]) % p

m = len(polynomial)-1 # stopień wielomianu
def get_sequence():
    T = p**m - 1 # okres sekwencji dla wielomianu
    
    complement = []
    for i in range(m):
        item = polynomial[i+1]
        complement.append(p-item)
    
    sequence = [i for i in start_sequence]
    len_of_start = len(start_sequence)
    for i in range(T-len_of_start):
        value = get_next(sequence, complement)
        sequence.append(value)
    
    length = len(sequence)
    return [sequence[i % length] for i in range(length*2)]
    
seq = get_sequence()


def get_seq(offset):
    if offset == -1:
        return [0 for _ in range(m)]
    return seq[offset:(offset+m)]

def get_seq_to_offset(q):
    seq_to_offset = dict()
    for i in range(-1, int(q-1)):
        seq_to_offset[tuple(get_seq(i))] = i
    return seq_to_offset

seq_to_offset = get_seq_to_offset(p ** m)


def add(p, m):
    q = int(p ** m)
    return [[add_value(i, j, p) for i in range(-1, q-1)] for j in range(-1, q-1)]

def add_value(i, j, p):
    si = get_seq(i)
    sj = get_seq(j)
    
    s_result = [(sj[ind] + si[ind]) % p for ind in range(len(sj))]
    offset_result = seq_to_offset[tuple(s_result)]
    
    if offset_result == -1:
        return "0 "
    if offset_result == 0:
        return "1 "
    return f'a{offset_result}'


def print_table(table, q, title):
    headers = [f'a{c}' for c in range(-1, q-1)]
    for i in range(len(headers)):
        header = headers[i]
        if header == "a-1":
            headers[i] = "0 "
        if header == "a0":
            headers[i] = "1 "
        
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

def show(p, m):
    print_table(add(p, m), p ** m, '+ ')
    
[show(p, m) for p in [2]]