# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
X = int(input())
list_size = Counter(input().split())

N = int(input())
total = 0
for i in range (N):
    value_size = input().split()
    size = value_size[0]
    value =int( value_size[1])
    if size in list_size and list_size[size]>0:
        total += value
        list_size[size] -= 1
    

print(total)
