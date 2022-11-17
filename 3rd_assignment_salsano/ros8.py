#IEV

with open('rosalind_iev.txt', 'r') as f:
    a = f.readline().strip().split()
    AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa = int(a[0]), int(a[1]), int(a[2]), int(a[3]), int(a[4]), int(a[5]) 
    n_off_pos = 0
    n_off_pos += 2*AA_AA
    n_off_pos += 2*AA_Aa
    n_off_pos += 2*AA_aa
    n_off_pos += 1.5*Aa_Aa 
    n_off_pos += Aa_aa
    print(n_off_pos)    
