#FIBD

with open('rosalind_fibd.txt', 'r') as f:
    a = f.readline().strip().split()
    n = int(a[0])
    m = int(a[1])

    liv = [1, 1]
    for el in range(2, n):
        tmp = liv[el-1] + liv[el-2]
        if el < m:
            tmp = tmp
        elif el > m:
            tmp = tmp- liv[el-m-1]
        else:
            tmp = tmp - 1
        liv.append(tmp)
    print(liv[-1])