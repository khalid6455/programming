# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *
AB = int(input())
BC = int(input())

print(str(round(degrees(atan(AB/BC))))+chr(176))
