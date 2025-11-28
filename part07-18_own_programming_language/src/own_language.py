import operator
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
    else:
        raise ValueError(f"Unknown assignment operation: {op}")


def check_expression(vars: Variables, *args: str) -> bool:
    op, a, b = args

    value1 = vars[a]
    value2 = int(b) if b.isdigit() else vars[b]

    OPERATORS = {
        "==": operator.eq,
        "!=": operator.ne,
        "<=": operator.le,
        ">=": operator.ge,
        "<": operator.lt,
        ">": operator.gt,
    }

    op_function = OPERATORS.get(op)

    if not op_function:
        raise ValueError(f"Unknown operator: {op}")

    return op_function(value1, value2)


def run(program: list[str]) -> Results:
    results: Results = []
    vars: Variables = {char: 0 for char in string.ascii_uppercase}
    locations: Locations = {
        instruction[:-1]: i
        for i, instruction in enumerate(program)
        if instruction.endswith(":")
    }
    position = 0

    while position < len(program):
        row = program[position]
        parts = row.split(" ")
        command = parts[0]

        if command == "END":
            # We reached the end of our program
            break
        elif command.endswith(":"):
            position += 1  # Ignore location markers
            continue

        if row.startswith("PRINT"):
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
