from datetime import datetime, timedelta

filename = input("Filename: ")
starting_date_str = input("Starting date: ")
day_count = int(input("How many days: "))

starting_date = datetime.strptime(starting_date_str, "%d.%m.%Y")
ending_date = starting_date + timedelta(day_count - 1)
timetable: dict[str, list[int]] = {}

print("Please type in screen time in minutes on each day (TV computer mobile):")

for days in range(day_count):
    period_date = starting_date + timedelta(days)
    date = period_date.strftime("%d.%m.%Y")

    screen_times = input(f"Screen time {date}: ")

    timetable[date] = [int(screen_time) for screen_time in screen_times.split(" ")]

total_minutes = sum(sum(screen_times) for _date, screen_times in timetable.items())
average_minutes = total_minutes / day_count

with open(filename, "w") as file:
    lines = []

    lines.append(
        f"Time period: {starting_date.strftime('%d.%m.%Y')}-{ending_date.strftime('%d.%m.%Y')}"
    )
    lines.append(f"Total minutes: {total_minutes}")
    lines.append(f"Average minutes: {average_minutes}")

    for date, screen_times in timetable.items():
        lines.append(f"{date}: {'/'.join(str(st) for st in screen_times)}")

    for line in lines:
        file.write(line + "\n")

print(f"Data stored in file {filename}")
