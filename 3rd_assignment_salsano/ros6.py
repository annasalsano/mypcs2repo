#IPRB

with open('rosalind_iprb.txt', 'r') as f:
    a = f.readline()
    a = a.split()
    lst = []
    for el in a:
        lst.append(el)
    k = int(lst[0])
    m = int(lst[1])
    n = int(lst[2])
    sum = k + m + n
    prb_homoA = k/sum*((k-1)/(sum-1))+ k/sum*(m/(sum-1)) + k/sum*(n/(sum-1))
    prb_eth = m/sum*(k/(sum-1)) + m/sum*((m-1)/(sum-1))*3/4 + m/sum*(n/(sum-1))*1/2
    prb_homoa = n/sum*(k/(sum-1)) + n/sum*(m/(sum-1))*1/2 + n/sum*((n-1)/(sum-1))*0
    fin_prob = prb_homoA + prb_eth + prb_homoa
    print(fin_prob)