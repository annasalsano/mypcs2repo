#SUBS

with open('rosalind_subs.txt', 'r') as f:
    a = f.readline().strip().split()
    b = f.readline().strip().split()
    seq = ''.join(a)
    subseq = ''.join(b)
    lst = []
    for k in range(len(seq)):
        j = len(subseq)
        a = seq[k : k+j]
        if a == subseq:
            lst.append(k+1)
    print(*lst)
