if __name__ == '__main__':
    n = int(input())
    students = []

    for _ in range(n):
        name = input()
        grade = float(input())
        students.append([name, grade])

    students.sort(key=lambda x: x[1])
    grades = sorted(set([student[1] for student in students]))

    second_lowest_grade = grades[1]
    names = [student[0] for student in students if student[1] == second_lowest_grade]

    names.sort()

    for name in names:
        print(name)
