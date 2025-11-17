name = input("Please tell me your name: ")

if name != "Jerry":
    portion_count = int(input("How many portions of soup? "))

    portion_cost = 5.9
    total_cost = portion_count * portion_cost

    print(f"The total cost is {total_cost}")

print("Next please!")
