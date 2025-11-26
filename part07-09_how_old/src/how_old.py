from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

date_of_birth = datetime(year, month, day)
eve_of_millennium = datetime(1999, 12, 31)
difference = eve_of_millennium - date_of_birth

if difference.days > 0:
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
