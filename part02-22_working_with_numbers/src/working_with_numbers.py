numbers_count = 0
numbers_sum = 0
positives_count = 0
negatives_count = 0


print("Please type in integer numbers. Type in 0 to finish.")


while True:
    number = int(input("Number: "))

    if number == 0:
        break

    numbers_count += 1
    numbers_sum += number

    if number > 0:
        positives_count += 1
    else:
        negatives_count += 1


print(f"Numbers typed in {numbers_count}")
print(f"The sum of the numbers is {numbers_sum}")

numbers_mean = numbers_sum / numbers_count
print(f"The mean of the numbers is {numbers_mean}")

print(f"Positive numbers  {positives_count}")
print(f"Negative numbers {negatives_count}")
