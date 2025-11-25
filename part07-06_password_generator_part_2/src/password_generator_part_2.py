from random import choice, randint, sample
from string import ascii_lowercase, digits


def generate_strong_password(length: int, numbers: bool, puns: bool) -> str:
    password: list[str] = []

    # Password must contain 1 lowercase letter
    password.append(choice(ascii_lowercase))

    if numbers:
        password.extend(sample(digits, k=randint(1, 3)))

    if puns:
        # Allowed special characters
        specials = "!?=+-()#"
        password.extend(sample(specials, k=randint(1, 3)))

    # Fill the rest with lowercase letters of length, minus the current
    # password length, as we could include 1-3 numbers or specials
    letters = sample(ascii_lowercase, length - len(password))
    password.extend(letters)

    return "".join(password)
