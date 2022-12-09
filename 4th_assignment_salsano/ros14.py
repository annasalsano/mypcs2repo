#PERM

import itertools 

with open('rosalind_perm.txt') as f:
    a = f.readline()
    b = int(a)
lst =[]
for el in range(1,b+1):
    lst.append(el)
perm = list(itertools.permutations(lst))
print(len(perm))
for el in perm:
    print(*el)