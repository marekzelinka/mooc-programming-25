class Course:
    def __init__(self, name: str, grade: int, credits: int) -> None:
        self.__name: str = name
        self.__grade: int = grade
        self.__credits: int = credits

    @property
    def name(self) -> str:
        return self.__name

    @property
    def grade(self) -> int:
        return self.__grade

    @property
    def credits(self) -> int:
        return self.__credits


class CourseRecords:
    def __init__(self) -> None:
        self.__courses: dict[str, Course] = {
            # "ItP": Course("ItP", 5, 5),
            # "ACiP": Course("ACiP", 1, 10),
            # "ItAI": Course("ItAI", 2, 5),
            # "Algo101": Course("Algo101", 4, 1),
            # "CompModels": Course("CompModels", 5, 8),
        }

    def add_record(self, name: str, grade: int, credits: int) -> None:
        if name not in self.__courses:
            self.__courses[name] = Course(name, grade, credits)

        course = self.__courses[name]

        if grade < course.grade:
            grade = course.grade

        self.__courses[name] = Course(name, grade, credits)

    def get_record(self, name: str) -> Course | None:
        return self.__courses.get(name)

    def all_entries(self) -> dict[str, Course]:
        return self.__courses

    def combined_credits(self) -> int:
        return sum(course.credits for course in self.__courses.values())

    def combined_grades(self) -> int:
        return sum(course.grade for course in self.__courses.values())

    def mean_grades(self) -> float:
        return self.combined_grades() / len(self.all_entries())

    def grades_chart(self) -> str:
        grades: list[int] = [0] * 5

        for course in self.__courses.values():
            grades[course.grade - 1] += 1

        chart = ""

        for course_grade in range(5, 0, -1):
            grades_count = grades[course_grade - 1]
            stars = "x" * grades_count

            chart += f"{course_grade}: {stars}\n"

        return chart


class CourseRecordsApplication:
    def __init__(self) -> None:
        self.__records: CourseRecords = CourseRecords()

    def help(self) -> None:
        print("commands: ")

        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")

    def add_record(self) -> None:
        name = input("course: ")
        grade = int(input("grade: "))
        credits = int(input("credits: "))

        self.__records.add_record(name, grade, credits)

    def search(self) -> None:
        name = input("course: ")

        course = self.__records.get_record(name)

        if not course:
            print("no entry for this course")

            return

        print(f"{course.name} ({course.credits} cr) grade {course.grade}")

    def stats(self) -> None:
        records_count = len(self.__records.all_entries())
        total_credits = self.__records.combined_credits()
        credits_mean = self.__records.mean_grades()

        print(f"{records_count} completed courses, a total of {total_credits} credits")
        print(f"mean {credits_mean:.1f}")
        print("grade distribution")
        print(self.__records.grades_chart())

    def execute(self) -> None:
        self.help()

        while True:
            print("")

            command = input("command: ")

            if command == "0":
                break
            elif command == "1":
                self.add_record()
            elif command == "2":
                self.search()
            elif command == "3":
                self.stats()
            else:
                self.help()


# course_records = CourseRecords()
# course_records.add_record("ItP", 3, 5)
# print(course_records.get_record("ItP"))
application = CourseRecordsApplication()
application.execute()
