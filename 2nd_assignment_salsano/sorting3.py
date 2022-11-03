#Insertion Sort - Part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    m = n-1
    for el in range(m):
        mine = arr[m]
        if mine < arr[m-1]:
            temp = arr[m]
            arr[m] = arr[m-1]
            print(' '.join(str(el) for el in arr))
            arr[m-1] = temp
            m = m-1
        
    print(' '.join(str(el) for el in arr))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
