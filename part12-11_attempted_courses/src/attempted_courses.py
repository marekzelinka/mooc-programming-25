class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return (
            f"{self.student_name}, grade for the course {self.course_name} {self.grade}"
        )


# Write your solution here
def names_of_students(attempts: list):
    return map(lambda attempt: attempt.student_name, attempts)


def course_names(attempts: list):
    return sorted(set(map(lambda attempt: attempt.course_name, attempts)))


if __name__ == "__main__":
    attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
    print(attempt.student_name)
    print(attempt.course_name)
    print(attempt.grade)
    print(attempt)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)
