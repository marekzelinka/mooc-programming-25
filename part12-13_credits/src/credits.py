from functools import reduce


class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"


if __name__ == "__main__":
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)

    print(attempt)
    print(attempt.course_name)
    print(attempt.credits)
    print(attempt.grade)


# Write your solution
def sum_of_all_credits(attempts: list):
    return reduce(lambda acc, curr: acc + curr.credits, attempts, 0)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)

    credit_sum = sum_of_all_credits([s1, s2, s3])

    print(f"The sum of all credits: {credit_sum}")


def sum_of_passed_credits(attempts: list):
    passed = filter(lambda attempt: attempt.grade >= 1, attempts)

    return reduce(lambda acc, curr: acc + curr.credits, passed, 0)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)

    credit_sum = sum_of_passed_credits([s1, s2, s3])

    print(f"The sum of passed credits: {credit_sum}")


def average(attempts: list):
    passed = list(filter(lambda attempt: attempt.grade >= 1, attempts))

    if not len(passed):
        return 0

    return reduce(lambda acc, curr: acc + curr.grade, passed, 0) / len(passed)


if __name__ == "__main__":
    s1 = CourseAttempt("Introduction to Programming", 5, 5)
    s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
    s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)

    ag = average([s1, s2, s3])

    print(f"Average grade for passed courses: {ag}")
