#REVP

from Bio import SeqIO

record = SeqIO.read('rosalind_revp.txt', 'fasta')
seq = str(record.seq)                       
rev_seq = str(record.seq.complement())          

for el in range(len(seq)):
    for wl in range(4, 13):
        seq_rev = seq[el : el+wl]
        f_rev = rev_seq[el: el+wl]
        if len(seq_rev) > 3:
            if f_rev == seq_rev[::-1]:
                print(el + 1, len(seq_rev))
