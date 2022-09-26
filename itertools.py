# Enter your code here. Read input from STDIN. Print output to STDOUT]
from itertools import *
A = list(map(int,input().split()))
B = list(map(int,input().split()))
AXB = tuple(product(A,B))
for i in AXB :
    print(i,end=' ')
