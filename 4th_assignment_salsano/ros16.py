#LGIS

with open('rosalind_lgis.txt', 'r') as f:
    n = int(f.readline().strip())
    a = list(f.readline().strip().split())
seq = [eval(el) for el in a]

m = [0] * n
for k in range(n - 2, -1, -1):
    for j in range(n - 1, k, -1):
        if seq[k] < seq[j] and m[k] <= m[j]:
            m[k] += 1
    max_v = max(m)
    result = []
    for i in range(n):
        if m[i] == max_v:
            result.append(seq[i])
            max_v -= 1
print(*result)

s = [0] * n
for x in range(n - 2, -1, -1):
    for y in range(n - 1, x, -1):
        if seq[x] > seq[y] and s[x] <= s[y]:
            s[x] += 1
    max_value = max(s)
    result2 = []
    for i in range(n):
        if s[i] == max_value:
            result2.append(seq[i])
            max_value -= 1
print(*result2)
