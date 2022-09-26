# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import * 
string = input().split()
strings = ''.join(sorted(list(string[0]))).upper()

for i in range(1,int(string[1])+1):
    permut = list(combinations(strings,i))
    for j in permut:
        print(''.join(j))
 
