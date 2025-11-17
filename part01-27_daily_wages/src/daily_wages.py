hourly_wage = float(input("Hourly wage: "))
hours_worked = int(input("Hours worked: "))
day_of_week = input("Day of the week: ")

daily_wage = hourly_wage * hours_worked

if day_of_week == "Sunday":
    daily_wage *= 2

print(f"Daily wages: {daily_wage} euros")
