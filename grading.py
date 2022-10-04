#!/bin/python3



#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents():
    # Write your code here

   

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    new_grade =[]
    for i in grades:
       
        if (i >= 38):
            n = (i//5+1)*5
            if (n-i < 3):
                new_grade.append(n)
            else:
                new_grade.append(i)
        else:
            new_grade.append(i)
    
    for j in new_grade:
        print(j)
gradingStudents()

    
