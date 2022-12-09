#LEXF

import itertools

with open('rosalind_lexf.txt', 'r') as f:
    a = f.readline().strip(). split()
    b = f.readline()
    a = list(itertools.product(a, repeat = int(b)))
    for el in a:
        print(''.join(el))