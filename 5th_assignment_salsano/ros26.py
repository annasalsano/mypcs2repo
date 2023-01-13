#MPRT

from Bio import SeqIO
import requests
import re

with open('rosalind_mprt.txt', 'r') as f:
    a = f.readlines()
    id = []
    for el in a:
        id.append(el.strip())

fst = []

'''fasta = resp
fasta_name = fst_1
fasta_names = fst'''

for k in range(len(id)):
    site = 'http://www.uniprot.org/uniprot/' + id[k] + '.fasta'
    data = requests.get(site)
    resp = data.text
    fst_1 = id[k] + '.fasta'
    fst.append(fst_1)

for j in fst:    
    with open(j, 'w') as file:
        file.write(resp)

subseq = re.compile(r'(?=(N[^P][ST][^P]))')
            
cntr = 0 
for k in fst:
    with open(k, 'r'):
        for el in SeqIO.parse(k, 'fasta'):
            sequence = el.seq
            pos = []
            for m in re.finditer(subseq, str(sequence)):
                pos.append(m.start() + 1)
            if len(pos) > 0:
                print(id[cntr])
                print(' '.join(map(str, pos)))
            cntr += 1
