#PROB

from collections import Counter
from math import log10

with open('rosalind_prob.txt', 'r') as f:
    a = f.readline().strip().split()
    seq = ''.join(a)
    b = f.readline().strip().split()
    
    fin = []
    b = [float(el) for el in b]

    for prob in b:
        outp = 0
        prb_dict = {'C': prob/2, 'G': prob/2, 'A': (1-prob)/2, 'T':(1-prob)/2}
        for nuc in seq:
            outp = outp + log10(prb_dict[nuc])
        fin.append(outp)
    print(' '.join([str(el) for el in fin]))
