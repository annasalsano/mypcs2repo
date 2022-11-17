#REVC

with open('rosalind_revc.txt', 'r') as f:
    a = f.readline().strip().split()
    seq = ''.join(a)

    u = seq.lower()
    for el in u:
        if el == 'a':
            u = u.replace(el,'T')
        elif el == 't':
            u = u.replace(el,'A')
        elif el == 'c':
            u = u.replace(el, 'G')
        elif el == 'g':
            u = u.replace(el, 'C')
    print(u[::-1])
