from itertools import *
N  = int(input())
string = input().split()
k = int(input())


element = list(combinations(string,k))
y = len(element)
sum = 0
for i in element:
    if 'a' in i:
        sum += 1
print(sum/y)
