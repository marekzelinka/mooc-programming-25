from json import loads


def print_persons(filename: str) -> None:
    with open(filename) as file:
        students = loads(file.read())

    for student in students:
        print(
            f"{student['name']} {student['age']} years ({', '.join(student['hobbies'])})"
        )


if __name__ == "__main__":
    print_persons("file1.json")
