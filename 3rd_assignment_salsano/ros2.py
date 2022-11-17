#RNA

with open('rosalind_rna.txt', 'r') as f:
    a = f.readline().strip().split()
    seq = ''.join(a)
    new_seq = seq.replace('T', 'U')
    print(new_seq)