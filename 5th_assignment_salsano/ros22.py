#PPER

with open('rosalind_pper.txt', 'r') as f:
    a = f.readline().strip().split()
    n = int(a[0])
    k = int(a[1])   

from itertools import permutations

cntr = 0

for el in permutations(range(1, n+1), k):
    cntr += 1

print(cntr % 1000000)