# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
n_roll_number = input().split()
b = int(input())
b_roll_number = input().split()
n_set = set(map(int,n_roll_number))
b_set = set(map(int,b_roll_number))
result = n_set.union(b_set)
print(len(result))
