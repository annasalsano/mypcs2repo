#CamelCase
#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'camelcase' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def camelcase(s):
    # Write your code here
    cntr = 0
    for let in s:
        if let.isupper() == True:
            cntr += 1
            
    return cntr +1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
