#GRPH

from Bio import SeqIO

rec = SeqIO.parse('rosalind_grph.txt', 'fasta')

all_seq = []
all_id = []

for el in rec:
    all_seq.append(el.seq)
    all_id.append(el.id)

print(all_seq)
print(all_id)

for k in range(len(all_seq)):
    for j in range(len(all_seq)):
        a = all_seq[k][-3:]
        if a == all_seq[j][:3]:
            if all_seq[k] == all_seq[j]:
                pass
            else:
                print(all_id[k], all_id[j])