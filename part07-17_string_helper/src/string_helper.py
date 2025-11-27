import string


def change_case(orig_string: str) -> str:
    return orig_string.swapcase()


def split_in_half(orig_string: str) -> tuple[str, str]:
    mid_point_index = len(orig_string) // 2

    return orig_string[0:mid_point_index], orig_string[mid_point_index:]


def remove_special_characters(orig_string: str) -> str:
    allowed = string.ascii_letters + string.digits + string.whitespace

    return "".join(char for char in orig_string if char in allowed)


if __name__ == "__main__":
    my_string = "Well hello there!"

    print(change_case(my_string))  # wELL HELLO THERE!

    p1, p2 = split_in_half(my_string)

    print(p1)  # Well hel
    print(p2)  # lo there!

    m2 = remove_special_characters("This is a test, lets see how it goes!!!11!")
    print(m2)  # This is a test lets see how it goes11
