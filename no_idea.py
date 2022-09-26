# Enter your code here. Read input from STDIN. Print output to STDOUT
from array import *
n = input().split()
element = map(int,input().split())

arr = array('i',element)
A = set(map(int,input().split()))
B = set(map(int,input().split()))

happinees = 0
for g in arr:
    if g in(A):
        happinees += 1
    elif (g in(B)):
        happinees -= 1
    else:
        happinees = happinees
print(happinees)
