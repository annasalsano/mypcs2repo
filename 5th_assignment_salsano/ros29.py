#LONG
  
from Bio import SeqIO

rec = SeqIO.parse('rosalind_long.txt', 'fasta')

seq = []

for el in rec:
    seq.append(el.seq)

segm = seq.pop(0)
l = len(segm)//2
j = 0

#for j in range(len(seq)):
while seq != []:
    s = seq[j]
    if seq == []:
        break
    if s[l:] in segm:
        segm = s + segm[segm.index(s[l:]) + len(s[l:]):]
        seq.remove(s)
        j = 0
        continue
    if s[:l] in segm:
        segm = segm[:segm.index(s[:l])] + s
        seq.remove(s)
        j = 0
        continue
    else:
        j += 1
print(segm)