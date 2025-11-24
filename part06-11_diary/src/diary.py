def add_entry() -> None:
    entry = input("Diary entry: ")

    with open("diary.txt", "a") as diary:
        diary.write(f"{entry}\n")

    print("Diary saved")


def read_entries() -> None:
    print("Entries:")

    with open("diary.txt") as diary:
        for entry in diary:
            print(entry.replace("\n", ""))


def quit() -> None:
    print("Bye now!")


while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")

    command = int(input("Function: "))

    if command == 1:
        add_entry()
    elif command == 2:
        read_entries()
    elif command == 0:
        quit()

        break
