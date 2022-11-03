#Min-Max Sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    new_list1 = []
    newlist2 = []

    arr.sort()
    for el in range(4):
        new_list1.append(arr.pop(0))

    narr = arr + new_list1
    narr.sort()

    for el2 in range(4):
        newlist2.append(narr.pop(-1))

    sum1 = sum(new_list1)
    sum2 = sum(newlist2)

    print(sum1, sum2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
