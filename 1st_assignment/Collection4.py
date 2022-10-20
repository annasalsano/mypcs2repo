#collections.Counter()

from collections import Counter

n_shoes = int(input())
sz_shoes = list(input().split())
n_cost = int(input())

Counter(sz_shoes)

money = []

for n in range(n_cost):
    size, price = input().split()
    for s in sz_shoes:
        if size == s:
            money.append(int(price))
            sz_shoes.remove(s)
            break
        else:
            pass
print(sum(money))