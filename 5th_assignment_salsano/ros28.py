#SSEQ

from Bio import SeqIO

rec = SeqIO.parse('rosalind_sseq.txt', 'fasta')

all_seq = []

for el in rec:
    all_seq.append(el.seq)

seq = all_seq[0]
subseq = all_seq[1]

j = 0

lst = []

for k in range(len(seq)):
    if seq[k] == subseq[j]:
        lst.append(int(k)+1)
        if len(lst) == len(subseq):
            break
        else:
            j += 1
    
print(*lst)