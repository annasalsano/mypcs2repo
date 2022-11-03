#Gemstones
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gemstones' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY arr as parameter.
#

def gemstones(arr):
    # Write your code here
    lst = []
    lst2 = []
    for el in arr:
        a = set(el)
        for x in a:
            lst.append(x)
    for el in lst:
        b = lst.count(el)
        if b == len(arr):
            if el in lst2:
                pass
            else:
                lst2.append(el)
    return len(lst2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
