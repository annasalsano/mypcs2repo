#Funny String

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    lst = []
    diff1 = []
    diff2 = []
    for car in s:
        lst.append(ord(car))
    for x in range(len(s) - 1):
        diff1.append(abs(lst[x] - lst[x+1]))
    lst.reverse()
    for k in range(len(s) - 1):
        diff2.append(abs(lst[k] - lst[k+1]))
    cntr = 0
    for j in range(len(diff1)):
        if diff1[j] == diff2[j]:
            pass
        else:
            cntr +=1
    if cntr != 0:
        return 'Not Funny'
    else:
        return 'Funny'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
