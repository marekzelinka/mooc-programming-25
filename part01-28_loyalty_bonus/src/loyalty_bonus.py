points = int(input("How many points are on your card? "))

factor = 1.1

if points < 100:
    print("Your bonus is 10 %")

if points >= 100:
    factor = 1.15
    print("Your bonus is 15 %")

points *= factor

print("You now have", points, "points")
