import csv
from datetime import datetime


def cheaters() -> list[str]:
    cheating_students: list[str] = []

    start_times: dict[str, str] = {}

    with open("start_times.csv") as file:
        for name, time_str in csv.reader(file, delimiter=";"):
            start_times[name] = time_str

    with open("submissions.csv") as file:
        for name, _task, _points, end_time_str in csv.reader(file, delimiter=";"):
            start_time = datetime.strptime(start_times[name], "%H:%M")
            end_time = datetime.strptime(end_time_str, "%H:%M")
            diff_in_hours = (end_time - start_time).total_seconds() / 60 / 60

            if diff_in_hours > 3 and name not in cheating_students:
                cheating_students.append(name)

    return cheating_students
