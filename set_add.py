# Enter your code here. Read input from STDIN. Print output to STDOUTsidle
N = int(input())

sets = set()
for i in range (N):
    name_of_country = input()
    sets.add(name_of_country)
print(len(sets))
