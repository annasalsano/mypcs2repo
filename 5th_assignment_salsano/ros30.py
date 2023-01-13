#PMCH

from Bio import SeqIO
from collections import Counter
from math import factorial

record = SeqIO.read('rosalind_pmch.txt', 'fasta')
seq = str(record.seq)

nuc = Counter(seq)
n_pyr = nuc['A']
n_pur = nuc['C']

tot = factorial(n_pyr) * factorial(n_pur)

print(tot)