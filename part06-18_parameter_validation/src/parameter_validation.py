def new_person(name: str, age: int) -> tuple[str, int]:
    if name.strip().isspace():
        raise ValueError("Name is required")
    elif len(name.split(" ")) < 2:
        raise ValueError("Name must be 2 or less characters long")
    elif len(name) > 50:
        raise ValueError("Name must be less than 50 characters long")

    if age < 0:
        raise ValueError("Age must be greater than 0")
    elif age > 150:
        raise ValueError("Age must be less than 150")

    return name, age
