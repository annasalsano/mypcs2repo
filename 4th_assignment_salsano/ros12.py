#HAMM

with open('rosalind_hamm.txt', 'r') as f:
    a = f.readline().strip()
    b = f.readline()
    cntr = 0
    for k in range(len(a)):
        if a[k] == b[k]:
            pass
        else:
            cntr += 1
    print(cntr)