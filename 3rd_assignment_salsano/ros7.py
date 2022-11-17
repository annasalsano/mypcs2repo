#LIA

from math import factorial

with open('rosalind_lia.txt', 'r') as f:
    a = f.readline().strip().split()
    k = int(a[0])
    n = int(a[1])
    tot = 2**k
    prob = []

    prb_AaBb = 1/4
    
    for r in range(n,(tot+1)):
        fact = factorial(tot)/factorial(r)/factorial(tot-r)
        prob.append(fact*(prb_AaBb**r)*((1-prb_AaBb)**(tot-r)))
    print(sum(prob))