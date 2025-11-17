temp_in_f = int(input("Please type in a temperature (F): "))

temp_in_c = (temp_in_f - 32) * 5 / 9

print(f"{temp_in_f} degrees Fahrenheit equals {temp_in_c} degrees Celsius")

if temp_in_c < 0:
    print("Brr! It's cold in here!")
