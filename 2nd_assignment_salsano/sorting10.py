#Closest Number
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def closestNumbers(arr):
    # Write your code here
    result = []
    arr.sort()
    for k in range(len(arr) - 1):
        if k == 0:
            min_diff = abs(arr[k+1] - arr[k])
        diff = abs(arr[k+1] - arr[k])
        if diff == min_diff:
            result.append(arr[k])   
            result.append(arr[k+1]) 
        if diff < min_diff:
            min_diff = diff
            result.clear()
            result.append(arr[k])
            result.append(arr[k+1])
        
    return result  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
