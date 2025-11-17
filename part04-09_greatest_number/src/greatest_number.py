def greatest_number(a: int, b: int, c: int) -> int:
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
