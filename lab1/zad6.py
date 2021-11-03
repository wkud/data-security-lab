'''
Wygenerować sekwencję okresową dla wielomianu nad ciałem GF(p). 
Wykorzystać zależność rekurencyjną stowarzyszoną z wielomianem. Przetesto¬wać 
działanie programu dla wielomianów o współczynnikach i sekwencji początkowej 
zadawanych przez użytkownika (wprowadzanych jako dane do programu lub zadawanych 
jako stałe w programie), np. dla   nad GF(2),   nad GF(3), lub innych
'''


from typing import Sequence


polynomial = [1, 2, 1]
start_sequence = [1, 0]
p=3

def get_next(sequence, complement):
    # sum = 0
    # for index in range(len(complement)):
    #     c = complement[index]
    #     s = sequence[-(index+1)]
    #     sum += c*s
    
    return sum([complement[index] * sequence[-(index+1)] for index in range(len(complement))]) % p

def show():
    m = len(polynomial)-1 # stopień wielomianu
    T = p**m # okres sekwencji
    
    complement = []
    for i in range(m):
        item = polynomial[i+1]
        complement.append(p-item)
    
    sequence = [i for i in start_sequence]
    len_of_start = len(start_sequence)
    for i in range(T-len_of_start):
        value = get_next(sequence, complement)
        sequence.append(value)
    
    print(sequence)
    
show()