#Compress the String!

from itertools import groupby

s = str(input()) + ' '

group = []
n = 1

for char in range(len(s) - 1):
    if s[char] == s[char + 1]:
        n = n + 1
    elif s[char] != s[char +1]:
        group.append((n, int(s[char])))
        n = 1
        
for couple in group:
    print(couple, end = ' ')