# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *
string = input()
new_list = list(string)

group = groupby(new_list)
for i,j in group:
    key = i
    length = len(list(j))
    print((length,int(key)),end=' ')
