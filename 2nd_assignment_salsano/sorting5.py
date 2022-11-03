#Running Time of Algorithms
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'runningTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def runningTime(arr):
    # Write your code here
    cntr = 0
    for k in range(1, n):
        j = k-1
        el = arr[k]
        while (j >= 0) and (arr[j] > el):
           arr[j+1] = arr[j]
           j = j - 1
           cntr += 1
        arr[j+1] = el
    return cntr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
