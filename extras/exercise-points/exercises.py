def read_weekly_points(filename: str) -> dict[str, list[int]]:
    weekly_points: dict[str, list[int]] = {}

    with open(filename) as my_file:
        for line in my_file:
            line = line.replace("\n", "")

            parts = line.split(";")

            student_name = parts[0]
            points = parts[1:]

            weekly_points[student_name] = [int(points) for points in points]

    return weekly_points


def course_grade(points: int) -> int:
    if points < 20:
        return 0
    elif points < 25:
        return 1
    elif points < 30:
        return 2
    elif points < 35:
        return 3
    elif points < 40:
        return 4
    else:
        return 5


def save_results(filename: str, weekly_points: dict[str, list[int]]) -> None:
    with open(filename, "w") as my_file:
        for name, points in weekly_points.items():
            total_points = sum(points)
            grade = course_grade(total_points)

            my_file.write(f"{name};{total_points};{grade}\n")


def get_grade(student_name: str, weekly_points: dict[str, list[int]]) -> int | None:
    for name, points in weekly_points.items():
        if name == student_name:
            total_points = sum(points)
            grade = course_grade(total_points)

            return grade


if __name__ == "__main__":
    weekly_points = read_weekly_points("weekly_points.csv")

    print(get_grade("Paula", weekly_points))
    save_results("results.csv", weekly_points)
