#Collections.namedtuple()

from collections import namedtuple

n_stud = int(input())
clmn = input().split()

print(sum([int(input().split()[clmn.index('MARKS')]) for n in range(n_stud)])/n_stud)