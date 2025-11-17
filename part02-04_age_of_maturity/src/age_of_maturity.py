age_of_maturity = 18

age = int(input("How old are you? "))

is_mature = age >= age_of_maturity

if is_mature:
    print("You are of age!")
else:
    print("You are not of age!")
