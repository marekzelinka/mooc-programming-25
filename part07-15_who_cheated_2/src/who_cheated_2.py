import csv
from datetime import datetime


def final_points() -> dict[str, int]:
    start_times: dict[str, str] = {}

    with open("start_times.csv") as file:
        for name, time_str in csv.reader(file, delimiter=";"):
            start_times[name] = time_str

    submissions = {}

    with open("submissions.csv") as file:
        for parts in csv.reader(file, delimiter=";"):
            name = parts[0]
            task = int(parts[1])
            points = int(parts[2])
            end_time = datetime.strptime(parts[3], "%H:%M")

            start_time = datetime.strptime(start_times[name], "%H:%M")
            difference_in_hours = (end_time - start_time).total_seconds() / 60 / 60

            if difference_in_hours > 3:
                continue

            if name not in submissions:
                submissions[name] = {}

            if task in submissions[name] and points < submissions[name][task]:
                continue

            submissions[name][task] = points

    return {student: sum(points.values()) for student, points in submissions.items()}
