#CONS

allseq = []
from Bio import SeqIO
from collections import Counter
import pandas as pd

f = SeqIO.parse('rosalind_cons.txt', 'fasta')
for el in f:
    allseq.append(el.seq)

cntr = []
for pos in range(len(allseq[0])):
    lst_pos = []
    for el in allseq:
        lst_pos.append(el[pos])
    c = Counter(lst_pos)
    cntr.append(c)

for pos in range(len(cntr)):
    print((cntr[pos]).most_common()[0][0], end='')
print()

dft = pd.DataFrame(cntr, columns=['A', 'C', 'G', 'T']).fillna(0).T
for symbol in ['A', 'C', 'G', 'T']:
    print(symbol, end=': ')
    dft.loc[symbol].apply(lambda row: print(int(row), end=' '))
    print()