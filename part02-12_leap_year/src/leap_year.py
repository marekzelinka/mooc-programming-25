year = int(input("Please type in a year: "))

is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print("That year is a leap year.")
else:
    print("That year is not a leap year.")
