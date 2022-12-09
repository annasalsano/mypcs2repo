#FIB

with open('rosalind_fib.txt', 'r') as f:
    a = f.readline().strip().split()
    n = int(a[0])
    k = int(a[1])

    gen = 1
    off_spr = 1
    for el in range(n - 1):
        off_spr, gen = gen, gen + (off_spr * k)
    print(off_spr)