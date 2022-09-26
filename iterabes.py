# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
N = int(input())
string  = list(input().split())
k = int(input())
sum = 0
for i in range(1,N):
    sum += i*pow(10,(N-i))
sum = list(str(sum))
sum = list(combinations(sum,k))
length = len(sum)
repet = 0
for i in sum:
    first = int(i[0])
    second = int(i[1])
    #print(string[first - 1:second - 1])
    if 'a' in string[first-1:second-1]:
        repet += 1
rt = repet/length
#print(repet)
print("{:.12f}".format(rt))




