from .typehints import Course


def add_student(students: dict[str, list[Course]], student: str) -> None:
    courses = []
    students[student] = courses


def print_student(students: dict[str, list[Course]], student: str) -> None:
    if student not in students:
        print(f"{student}: no such person in the database")

        return

    courses = students[student]

    print(f"{student}:")

    if len(courses) == 0:
        print(" no completed courses")

        return

    print(f" {len(courses)} completed courses:")

    for student, grade in courses:
        print(f"  {student} {grade}")

    average_grade = sum([course[1] for course in courses]) / len(courses)

    print(f" average grade {average_grade}")


def add_course(students: dict[str, list[Course]], student: str, course: Course) -> None:
    updated_courses: list[Course] = []

    students[student].append(course)

    sorted_courses = sorted(
        students[student], key=lambda course: course[1], reverse=True
    )

    for subject, grade in sorted_courses:
        courses = list(filter(lambda course: course[0] == subject, updated_courses))

        if len(courses) != 0 or grade == 0:
            continue

        updated_courses.append((subject, grade))

    students[student] = updated_courses


def summary(students: dict[str, list[Course]]) -> None:
    print(f"students {len(students)}")

    first_student = list(students)[0]

    most_courses_completed = (first_student, len(students[first_student]))
    best_average_grade = (
        first_student,
        sum([course[1] for course in students[first_student]])
        / len(students[first_student]),
    )

    for student, courses in students.items():
        if len(courses) > most_courses_completed[1]:
            most_courses_completed = (student, len(courses))

        average_grade = sum([course[1] for course in courses]) / len(courses)

        if average_grade > best_average_grade[1]:
            best_average_grade = (student, average_grade)

    print(
        f"most courses completed {most_courses_completed[1]} {most_courses_completed[0]}"
    )
    print(f"best average grade {best_average_grade[1]} {best_average_grade[0]}")


def main() -> None:
    students: dict[str, list[Course]] = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    print_student(students, "Peter")
    print_student(students, "Eliza")
    print_student(students, "Jack")

    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Peter", ("Introduction to Programming", 3))
    add_course(students, "Peter", ("Advanced Course in Programming", 2))
    add_course(students, "Peter", ("Introduction to Programming", 2))

    add_course(students, "Peter", ("Data Structures and Algorithms", 0))

    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    print_student(students, "Peter")
    summary(students)


if __name__ == "__main__":
    main()
