#Collection.OrderDict()

from collections import OrderedDict
N_items = int(input())
dct = OrderedDict()
for n in range(N_items):
    row = input().split()
    price = (int(row[-1]))
    item = ' '.join(row[0:-1])
    if item in dct:
        dct[item] += price
    else:
        dct[item] = price
for key, value in dct.items():
    print(key, value)