def parse_inputs(result: str) -> tuple[int, int]:
    value_a, value_b = result.split(" ")

    exam_points = int(value_a)

    if exam_points < 0 and exam_points < 20:
        raise ValueError("Exam points must be between 0 and 20.")

    exercises_completed = int(value_b)

    if exercises_completed < 0 and exercises_completed > 100:
        raise ValueError("Exercises completed must be between 0 and 100.")

    return exam_points, exercises_completed


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


def course_result() -> tuple[list[int], list[int]]:
    points: list[int] = []
    # We have 6 possible grades: 0 (fail), 1, 2, 3, 4, 5; we initialize the
    # array with zeros (0), later when we have the grade, based on points, we
    # can update the count.
    grades: list[int] = [0] * 6

    while True:
        result = input("Exam points and exercises completed: ")

        if result == "":
            break

        exam_points, exercises_completed = parse_inputs(result)

        exercise_points = exercises_completed // 10
        total_points = exam_points + exercise_points

        points.append(total_points)
        grade = course_grade(total_points)

        # If a student recived less that 10 points, they fail the course.
        if exam_points < 10:
            grade = 0

        grades[grade] += 1

    return points, grades


def grades_chart(grades: list[int]) -> str:
    chart = ""

    for course_grade in range(5, -1, -1):
        grades_count = grades[course_grade]
        stars = "*" * grades_count

        chart += f"  {course_grade}: {stars}\n"

    return chart


def course_stats(points: list[int], grades: list[int]) -> str:
    stats: str = ""

    points_average = sum(points) / len(points)
    pass_percentage = 100 * (len(points) - grades[0]) / len(points)
    chart = grades_chart(grades)

    stats += "Statistics:\n"
    stats += f"Points average: {points_average:.1f}\n"
    stats += f"Pass percentage: {pass_percentage:.1f}\n"
    stats += "Grade distribution:\n"
    stats += f"{chart}\n"

    return stats


def main() -> None:
    points, grades = course_result()
    stats = course_stats(points, grades)

    print(stats)


main()

if __name__ == "__main__":
    main()
