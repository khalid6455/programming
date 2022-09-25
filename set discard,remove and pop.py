n = int(input())
s = set(map(int, input().split()))
N = int(input())
for i in range (N):
    comand = input().split()
    if comand[0] == 'pop':
        s.pop()
    elif comand[0] == 'remove':
        s.remove(int(comand[1]))
    elif comand[0] == 'discard':
        s.discard(int(comand[1]))
sum = 0
for i in s:
    sum += i
print(sum)
