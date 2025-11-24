def store_personal_data(person: tuple[str, int, float]) -> None:
    line = f"{person[0]};{person[1]};{person[2]}"

    with open("people.csv", "a") as file:
        file.write(f"{line}\n")
