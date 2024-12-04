n = int(input())
student_marks = {}
for i in range(n):
    name, *marks = input().split()
    marks = list(map(float,marks))
    student_marks[name] = marks
    
query_name = input().strip()
query_marks = student_marks[query_name]
average = sum(query_marks)/ len(query_marks)
print(average)

    