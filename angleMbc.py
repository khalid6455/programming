# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import *
AB = int(input())
BC = int(input())
oposite = (sqrt(pow(AB,2)+pow(BC,2)))/2
print(str(round(degrees(asin(oposite/BC))))+chr(176))
