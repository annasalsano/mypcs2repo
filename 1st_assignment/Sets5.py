#Check Subsets

n_test = int(input())
for n in range(n_test):
    n_el_A = input()
    el_A = input().split()
    A = set(el_A)

    n_el_B = input()
    el_B = input().split()
    B = set(el_B)

    print(A.issubset(B))
