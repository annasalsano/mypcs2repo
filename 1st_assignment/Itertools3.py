#itertools.permutations()

from itertools import permutations
s, n = input().split()
for el in sorted(list(permutations(s, int(n)))):
    print(''.join(el))