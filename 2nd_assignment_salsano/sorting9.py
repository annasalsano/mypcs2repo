#Find the Median
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    arr = sorted(arr)
    
    for n in range(len(arr)//2):
        arr.remove(arr[0])
        arr.remove(arr[-1])
    print(*arr)
    
if __name__ == '__main__':
    
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)
