#SPLC

from Bio import SeqIO

rec = SeqIO.parse('rosalind_splc.txt', 'fasta')
all_seq = []

for el in rec:
    all_seq.append(el.seq)

seq = all_seq[0]
introns = []

for el in range(1, len(all_seq)):
    introns.append(all_seq[el])

for el in range(len(introns)):
    for k in range(len(seq)):
        if seq[k:k+len(introns[el])] == introns[el]:
            seq = seq.replace(str(seq[k:k+len(introns[el])]), '')

print(seq.translate())