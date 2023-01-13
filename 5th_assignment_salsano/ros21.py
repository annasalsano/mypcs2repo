#ORF

from Bio import SeqIO

rec = SeqIO.read('rosalind_orf.txt', 'fasta')

seq = rec.seq

rna_seq = seq.transcribe()
rev_seq = seq.reverse_complement().transcribe()

rna = []
rna2=[]
mrna = []
mrna2=[]

for k in range(0,3):
    for i in range(k, len(rna_seq), 3):
        a = rna_seq[i: i+3]
        if a == 'AUG':
            rna.append(rna_seq[i:])
for k in range(len(rna)):
    for el in range(0, len(rna[k]), 3):
        a = rna[k][el: el+3]
        if a == 'UAA' or a == 'UAG' or a == 'UGA':
            mrna.append(rna[k][:el])
            break
        
for k in range(0,3):
    for i in range(k, len(rev_seq), 3):
        a = rev_seq[i: i+3]
        if a == 'AUG':
            rna2.append(rev_seq[i:])
for k in range(len(rna2)):
    for el in range(0, len(rna2[k]), 3):
        a = rna2[k][el: el+3]
        if a == 'UAA' or a == 'UAG' or a == 'UGA':
            mrna2.append(rna2[k][:el])
            break
        
prot = []

for el in mrna:
    sett = el.translate()
    if sett in prot:
        pass
    else:
        prot.append(sett)

for k in mrna2:
    sett = k.translate()
    if sett in prot:
        pass
    else:
        prot.append(sett)
    
for el in prot:
    print(el)


'''
prot = rna_seq.translate()
print(prot)

prot = seq.translate(to_stop=True)
print(prot)

for i in range(len(rna_seq)):
    a = rna_seq[i: i+3]
    if a == 'AUG':
        rna.append(rna_seq[i+3:])

for el in mrna:
    if 'UAA' or 'UAG' or 'UGA' in el:

for el in range(len(mrna)):
    a = mrna[el: el+3]
    if a == 'UAA' or a == 'UAG' or a == 'UGA':
        mrna.append(rna_seq[i+3:])

mrna = rna.rsplit('UAG')
mrna = rna.rsplit('UAA')
mrna = rna.rsplit('UGA')
'''