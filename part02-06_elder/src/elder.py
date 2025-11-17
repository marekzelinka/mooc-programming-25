print("Person 1:")

person_a_name = input("Name: ")
person_a_age = int(input("Age: "))

print("Person 2:")

person_b_name = input("Name: ")
person_b_age = int(input("Age: "))

if person_a_age > person_b_age:
    print(f"The elder is {person_a_name}")
elif person_b_age > person_a_age:
    print(f"The elder is {person_b_name}")
else:
    print(f"{person_a_name} and {person_b_name} are the same age")
