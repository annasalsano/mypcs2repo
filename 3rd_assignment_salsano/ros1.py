#DNA

from collections import Counter
with open('rosalind_dna.txt', 'r') as f:
    a = f.readline().strip().split()
    seq = ''.join(a)
    nuc = Counter(seq)

    o_nuc = sorted(nuc.items())

    for k in range(1):
        print(o_nuc[k][1], o_nuc[k+1][1], o_nuc[k+2][1], o_nuc[k+3][1])