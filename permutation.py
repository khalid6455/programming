# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import * 
string = input().split()
strings = ''.join(sorted(list(string[0])))

permut = list(permutations(strings,int(string[1])))
for i in permut:
    print(''.join(i))
