if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list = []
    for i in arr:
        if i not in list:
            list.append(i)
    list.sort()
    length = len(list)
    print(list[length-2])
