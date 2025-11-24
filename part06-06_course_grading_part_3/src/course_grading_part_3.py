if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
    exam_data = input("Exam points: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
    exam_data = "exam_points1.csv"

students: dict[int, str] = {}

with open(student_info) as file:
    for line in file:
        parts = line.split(";")

        if parts[0] == "id":
            # Ignore csv header
            continue

        id = int(parts[0])
        first, last = parts[1:]

        students[id] = f"{first} {last}".strip()

exercises: dict[int, int] = {}

with open(exercise_data) as file:
    for line in file:
        parts = line.split(";")

        if parts[0] == "id":
            # Ignore csv header
            continue

        id = int(parts[0])
        points = [int(grade) for grade in parts[1:]]

        exercises[id] = sum(points)

exams_points: dict[int, int] = {}

with open(exam_data) as file:
    for line in file:
        parts = line.split(";")

        if parts[0] == "id":
            # Ignore csv header
            continue

        id = int(parts[0])
        points = [int(point) for point in parts[1:]]

        exams_points[id] = sum(points)


def course_grade(points: int) -> int:
    # Grade is determined based on points:
    # - if we recived more or equal than 28 (up to 30), the grade is 5 (pass)
    # - if we recived more or equal than 24 (up to 27), the grade is 4 (pass)
    # - if we recived more or equal than 21 (up to 23), the grade is 3 (pass)
    # - if we recived more or equal than 18 (up to 20), the grade is 2 (pass)
    # - if we recived more or equal than 15 (up to 17), the grade is 1 (pass)
    # - if we recived more or equal than 0 (up to 14), the grade is 0 (fail)
    boundary = [0, 15, 18, 21, 24, 28]

    for grade in range(5, -1, -1):
        if points >= boundary[grade]:
            return grade

    return 0


# Print out the stats header
print(
    "name".ljust(30),
    "exec_nbr".ljust(10),
    "exec_pts.".ljust(10),
    "exm_pts.".ljust(10),
    "tot_pts.".ljust(10),
    "grade".ljust(10),
    sep="",
)

for id, name in students.items():
    exercises_completed = exercises.get(id, 0)
    points = exams_points.get(id, 0)
    exercise_points = exercises_completed // 4
    total_points = points + exercise_points
    grade = course_grade(total_points)

    print(
        f"{name:30}{exercises_completed:<10}{exercise_points:<10}{points:<10}{total_points:<10}{grade:<10}"
    )
