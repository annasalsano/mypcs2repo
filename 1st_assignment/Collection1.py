#Collection.deque()

from collections import deque
d = deque()
for data in range(int(input())):
    comm = input().split()
    if comm[0] == 'append':
        d.append(int(comm[1]))
    elif comm[0] == 'appendleft':
        d.appendleft(int(comm[1]))
    elif comm[0] == 'pop':
        d.pop()
    elif comm[0] == 'popleft':
        d.popleft()
for n in d:
    print(n, end = ' ')