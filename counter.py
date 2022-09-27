# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
X = int(input())
list_size = input().split()

N = int(input())
lists = []
for i in range (N):
    value_size = input()
    lists.append(value_size)
total = 0
for j in lists:
    x = j.split()
    
    if(x[0] in list_size ):
        total += int(x[1])
        list_size.remove(x[0])
    else:
        total =total
print(total)
