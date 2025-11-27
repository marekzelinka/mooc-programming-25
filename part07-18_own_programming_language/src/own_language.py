import string

from .types import Locations, Results, Variables


def print_command(results: Results, vars: Variables, var: str) -> None:
    results.append(int(var) if var.isdigit() else vars[var])


def assignment(vars, *args: str):
    op, a, b = args

    value = int(b) if b.isdigit() else vars[b]

    if op == "MOV":
        vars[a] = value
    elif op == "ADD":
        vars[a] += value
    elif op == "SUB":
        vars[a] -= value
    elif op == "MUL":
        vars[a] *= value


def check_expression(vars: Variables, *args: str) -> bool:
    op, a, b = args

    value1 = vars[a]
    value2 = int(b) if b.isdigit() else vars[b]

    result = False

    if "=" in op:
        if op == "==":
            result = value1 == value2
        elif "!" in op:
            result = value1 != value2
        elif "<" in op:
            result = value1 <= value2
        elif ">" in op:
            result = value1 >= value2
    elif "<" in op:
        result = value1 < value2
    elif ">" in op:
        result = value1 > value2

    return result


def run(program: list[str]) -> Results:
    results: Results = []
    vars: Variables = {char: 0 for char in string.ascii_uppercase}

    locations: Locations = {
        position[:-1]: program.index(position)
        for position in program
        if position.endswith(":")
    }

    position = 0

    while position < len(program):
        row = program[position]

        parts = row.split(" ")

        if row == "END":
            # We reached the end of our program
            #
            break
        elif row.endswith(":"):
            # LOCATION command: we ignore the location commands, because we already have them setup
            #
            pass
        elif row.startswith("PRINT"):
            # PRINT command: we first figure out if we are printing
            # a number or a variable and then add the variable it to results.

            var = parts[1]

            print_command(results, vars, var)
        elif row.startswith("IF"):
            op = parts[2]

            arg1 = parts[1]
            arg2 = parts[3]

            condition = check_expression(vars, op, arg1, arg2)

            if condition:
                goto = parts[5]
                position = locations[goto]
        elif row.startswith("JUMP"):
            goto = parts[1]
            position = locations[goto]
        else:
            # MOV, ADD, SUB, or MUL command: we pass the command and
            # the arguemnts and update our variables

            assignment(vars, *parts)

        position += 1

    return results
