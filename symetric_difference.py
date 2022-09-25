# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
m_integer = input().split()
n = int(input())
n_integer = input().split()
m_set = set(list(map(int,m_integer)))
n_set = set(list(map(int,n_integer)))
unio = m_set.union(n_set)
intersectio = m_set.intersection(n_set)
symetric_differernce = unio.difference(intersectio) 
new_list = list(symetric_differernce)
new_list.sort()
for i in new_list:
    print(i)
