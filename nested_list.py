if __name__ == '__main__':
    records = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,float(score)])
    
    list_number = []
    for i in range(len(records)):
        list_number.append(records[i][1])
    list_number.sort()
    second_lowest = list_number[1]
    names = []
    for i in range (len(records)):
        if(second_lowest == records[i][1]):
            names.append(records[i][0])
    names.sort()
    for i in names:
        print(i)
