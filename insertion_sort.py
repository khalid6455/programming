#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1():
    # Write your code here

    if __name__ == '__main__':
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

    store = arr[n-1]
    arr.remove(store)
    for i in range(n-2,-1,-1):
        if arr[i] < store:
            arr.insert(i+1,store)
            for j in arr:
                print(j,end=' ')
            break
        else:
            arr.insert(i+1,arr[i])
        for k in arr:
            print(k,end=' ')
        print()   
        arr.pop(i)
    if(store < arr[0]):
        arr.insert(0,store)
        for i in arr:
            print(i,end=' ')
insertionSort1()
