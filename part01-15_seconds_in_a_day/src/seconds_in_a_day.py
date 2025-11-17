day_count = int(input("How many days? "))

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
seconds_in_day = hours_in_day * minutes_in_hour * seconds_in_minute

seconds_in_days = seconds_in_day * day_count

print(f"Seconds in that many days: {seconds_in_days}")
