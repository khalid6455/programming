if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for key in student_marks:
        if key == query_name:
            value = student_marks[key]
    sum = 0
    for i in value:
        sum += i
    average = sum/3
    print(format(average,'.2f'))
