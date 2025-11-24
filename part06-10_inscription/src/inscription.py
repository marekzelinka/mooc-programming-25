name = input("Whom should I sign this to: ")
filename = input("Where shall I save it: ")

with open(filename, "w") as file:
    file.write(
        f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"
    )
