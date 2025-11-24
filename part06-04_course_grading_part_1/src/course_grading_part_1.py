student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")


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
        grades = [int(grade) for grade in parts[1:]]

        exercises[id] = sum(grades)

for id, name in students.items():
    completed_exercises = exercises.get(id, 0)

    print(f"{name} {completed_exercises}")
