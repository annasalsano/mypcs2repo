#TRAN
 
from Bio import SeqIO

rec = SeqIO.parse('rosalind_tran.txt', 'fasta')

all_seq = []
for el in rec:
    all_seq.append(el.seq)

seq1 = all_seq[0]
seq2 = all_seq[1]

transi = 0
transv = 0

for k in range(len(seq1)):
    if seq1[k] != seq2[k]:
        if seq1[k] == 'A' and seq2[k] == 'G':
            transi += 1
        elif seq1[k] == 'C' and seq2[k] == 'T':
            transi += 1 
        elif seq1[k] == 'G' and seq2[k] == 'A':
            transi += 1 
        elif seq1[k] == 'T' and seq2[k] == 'C':
            transi += 1
        else: 
            transv += 1
 
print(transi/transv)

'''
        if seq1[k] == 'A' and seq2[k] == 'T' or seq2[k] == 'C':
            transv += 1
        elif seq1[k] == 'G' and seq2[k] == 'C' or seq2[k] == 'T':
            transv += 1
        elif seq1[k] == 'C' and seq2[k] == 'A' or seq2[k] == 'G':
            transv += 1
        elif seq1[k] == 'T' and seq2[k] == 'A' or seq2[k] == 'G':
            transv += 1
        elif seq1[k] == 'A' and seq2[k] == 'G' or seq1[k] == 'C' and seq2[k] == 'T' or seq1[k] == 'G' and seq2[k] == 'A' or seq1[k] == 'T' and seq2[k] == 'C':
            '''