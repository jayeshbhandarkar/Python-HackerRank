from collections import namedtuple

n = int(input())
columns = input().split()

Student = namedtuple('Student', columns)

total_marks = 0
for _ in range(n):
    student = Student(*input().split())
    total_marks += int(student.MARKS)

average_marks = total_marks / n
print(f"{average_marks:.2f}")
