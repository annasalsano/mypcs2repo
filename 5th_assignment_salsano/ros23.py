#TREE

with open('rosalind_tree.txt', 'r') as f:
    n = int(f.readline())
    ad_list = []
    for line in f:
        lst = [int(x) for x in line.split()]
        ad_list.append(lst)

print(n - len(ad_list) - 1)