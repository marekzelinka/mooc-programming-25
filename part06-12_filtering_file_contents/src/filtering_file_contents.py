def read_solutions() -> list:
    solutions = []

    with open("solutions.csv") as file:
        for line in file:
            line = line.replace("\n", "")

            parts = line.split(";")

            name = parts[0]
            problem = parts[1]
            result = int(parts[2])
            solution = [name, problem, result]

            solutions.append(solution)

    return solutions


def check_result(problem: str, result: int) -> bool:
    if "+" in problem:
        a, b = [int(n) for n in problem.split("+")]

        check = a + b
    else:
        a, b = [int(n) for n in problem.split("-")]

        check = a - b

    return check == result


def write_solutions(filename: str, solutions):
    with open(filename, "w") as file:
        for solution in solutions:
            line = f"{solution[0]};{solution[1]};{solution[2]}"

            file.write(f"{line}\n")


def filter_solutions() -> None:
    solutions = read_solutions()

    correct_solutions = []
    incorrect_solutions = []

    for student, problem, result in solutions:
        correct = check_result(problem, result)

        if correct:
            correct_solutions.append([student, problem, result])
        else:
            incorrect_solutions.append([student, problem, result])

    write_solutions("correct.csv", correct_solutions)
    write_solutions("incorrect.csv", incorrect_solutions)
