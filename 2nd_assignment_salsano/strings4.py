#Mars Exploration
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    #fare 2 for loop... 1 per dire per ogni tripletta, e uno per dire per ogni carattere
    a = len(s)
    lst = [s[idx:idx + 3] for idx in range(0, a, 3)]
    cntr = 0
    for x in lst:
        if x == 'SOS':
            pass
        else:
            if x[0] != 'S':
                cntr += 1
            if x[1] != 'O':
                cntr += 1
            if x[2] != 'S':
                cntr += 1
    return cntr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
