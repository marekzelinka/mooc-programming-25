def parse_int(n: str) -> int:
    try:
        return int(n)
    except ValueError:
        return -1


def filter_incorrect():
    correct = []

    with open("lottery_numbers.csv") as file:
        for line in file:
            line = line.replace("\n", "")

            header, number_strs = line.split(";")

            label, week = header.split(" ")

            if label != "week":
                continue

            if parse_int(week) == -1:
                continue

            numbers = number_strs.split(",")

            found_incorrect = False

            for n in numbers:
                number = parse_int(n)
                print(f"{number}")

                if not (number >= 1 and number <= 39):
                    found_incorrect = True

                    break

            if found_incorrect:
                continue

            if len(numbers) < 7 or len(numbers) != len(set(numbers)):
                continue

            correct.append(line)

    with open("correct_numbers.csv", "w") as file:
        for line in correct:
            file.write(f"{line}\n")
