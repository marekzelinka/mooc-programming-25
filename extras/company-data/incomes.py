names = {}

with open("./employees.csv") as file:
    for line in file:
        parts = line.split(";")

        if parts[0] == "pic":
            # Ignore csv header
            continue

        pic = parts[0]
        name = parts[1]

        names[pic] = name

salaries = {}

with open("./salaries.csv") as file:
    for line in file:
        parts = line.split(";")

        if parts[0] == "pic":
            # Ignore csv header
            continue

        pic = parts[0]
        salary = int(parts[1])
        bonus = int(parts[2])

        salaries[pic] = salary + bonus

print("incomes:")

for pic, name in names.items():
    salary = salaries.get(pic, 0)

    print(f"{name:16} {salary} euros")
