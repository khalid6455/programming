#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort():
    # Write your code here

    if __name__ == '__main__':
        

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))
    
    result = [0]*(n)
    for j in arr:
        for i in range(n):
            if j == i:
                result[j] = result[j]+1
                break
    for i in result:
        print(i,end=' ')    
        
        
countingSort()

   
