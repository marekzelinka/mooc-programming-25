from random import sample
from string import ascii_lowercase


def generate_password(size: int) -> str:
    password_letters = sample(ascii_lowercase, size)

    return "".join(password_letters)
