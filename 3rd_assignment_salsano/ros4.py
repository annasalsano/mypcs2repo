#GC content

with open('seq.fasta', 'r') as f:
    a = f.readlines()

    fdict = {}

    for el in a:
        if '>' in el:
            label = el[1:-1]
            fdict[label] = ''
        else:
            if '\n' in el:
                el = el[:-1]
            fdict[label] += el

    tot_perc = []

    for key in fdict.values():
        sum = key.count('G') + key.count('C')
        perc = sum/len(key)*100
        tot_perc.append(perc)

    index = tot_perc.index(max(tot_perc))
    print(list(fdict)[index])
    print(max(tot_perc))