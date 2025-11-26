import urllib.request
from json import loads
from math import floor


def retrieve_all() -> list[tuple[str, str, int, int]]:
    base_url = "https://studies.cs.helsinki.fi/stats-mock/api/courses"

    response = urllib.request.urlopen(base_url)
    data = response.read()

    courses = loads(data)

    return [
        (course["fullName"], course["name"], course["year"], sum(course["exercises"]))
        for course in courses
        if course["enabled"]
    ]


def retrieve_course(course_name: str) -> dict[str, int]:
    base_url = (
        f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    )

    response = urllib.request.urlopen(base_url)
    data = response.read()

    course = loads(data)

    week_count = len(course)
    total_students = max(week["students"] for week in course.values())
    total_hours = sum(week["hour_total"] for week in course.values())
    hours_average = floor(total_hours / total_students)
    total_exercises = sum(week["exercise_total"] for week in course.values())
    exercises_average = floor(total_exercises / total_students)

    return {
        "weeks": week_count,
        "students": total_students,
        "hours": total_hours,
        "hours_average": hours_average,
        "exercises": total_exercises,
        "exercises_average": exercises_average,
    }


if __name__ == "__main__":
    retrieve_course("docker2019")
