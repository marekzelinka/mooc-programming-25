def balanced_brackets(my_string: str) -> bool:
    # if string is empty, all brackets are pairs
    if len(my_string) == 0:
        return True

    # the first character is not a bracket, skipping it
    if my_string[0] not in "()[]":
        return balanced_brackets(my_string[1:])

    # the last character is not a bracket, skipping it
    if my_string[-1] not in "()[]":
        return balanced_brackets(my_string[:-1])

    # the first and last characters are brackets, check if they are a pair
    if not (
        (my_string[0] == "(" and my_string[-1] == ")")
        or (my_string[0] == "[" and my_string[-1] == "]")
    ):
        return False

    # the brackets are not a pair, skip the first and last character and try again
    return balanced_brackets(my_string[1:-1])


if __name__ == "__main__":
    ok = balanced_brackets("([([])])")
    print(ok)

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)
