def add_entry(entry: str) -> None:
    with open("diary.txt", "a") as diary:
        diary.write(f"{entry}\n")

    # Handle errors and if success that print
    print("Diary saved")


def read_entries() -> None:
    with open("diary.txt") as diary:
        for entry in diary:
            print(entry.replace("\n", ""))


def quit() -> None:
    # Cleanups and closing message
    print("Bye now!")


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")

    command = int(input("Function: "))

    if command == 1:
        entry = input("Diary entry: ")

        add_entry(entry)
    elif command == 2:
        print("Entries:")

        read_entries()
    elif command == 0:
        quit()

        break
