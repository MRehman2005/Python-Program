# Step 1: Read the input
n = int(input())  # Number of students
students = []

for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Step 2: Sort the students by grade, then by name
students.sort(key=lambda x: (x[1], x[0]))

# Step 3: Find the second-lowest grade
lowest_grade = students[0][1]
second_lowest = None

# Loop through to find the second-lowest grade
for student in students:
    if student[1] > lowest_grade:
        second_lowest = student[1]
        break

# Step 4: Collect all students with the second-lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest]

# Step 5: Print the names of the students with the second-lowest grade, in alphabetical order
for student in sorted(second_lowest_students):
    print(student)
