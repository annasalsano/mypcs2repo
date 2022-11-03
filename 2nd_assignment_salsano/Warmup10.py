#Time Conversion
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    spl = s.split(':')
    
    if s[-2] == 'A':
        s = re.split('AM',s)
        if spl[0] == '12':
            spl[0] = '00'
            fin = f"{spl[0]}:{spl[1]}:{spl[2]}"
            return fin[:-2]
        else:
            return s[0]
    elif s[-2] == 'P':
        s = re.split('PM',s)
        if spl[0] == '12':
            return s[0]
        else:
            fin2 = f"{int(spl[0]) + 12}:{spl[1]}:{spl[2]}"
            return fin2[:-2]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
