#LCSM

from Bio import SeqIO

allseq = []
f = SeqIO.parse('rosalind_lcsm.txt', 'fasta')
for el in f:
    allseq.append(el.seq)

mtrx = [[0 for i in range(len(allseq[0]) +1)]
            for j in range(len(allseq[1]) +1)]

length, row, col = 0, 0, 0

for i in range(len(allseq[0]) +1):
    for j in range(len(allseq[1]) +1):
        if i == 0 or j == 0:
            mtrx[i][j] = 0
        else: 
            if allseq[0][i -1] == allseq[1][j -1]:
                mtrx[i][j] = mtrx[i-1][j-1] +1
                if length < mtrx[i][j]:
                    length = mtrx[i][j]
                    row = i
                    col = j
            else:
                mtrx[i][j] = 0

res = ['0']*length
while mtrx[row][col] != 0:
    length -= 1
    res[length] = allseq[0][row -1]
    row -= 1
    col -= 1
print(''.join(res))