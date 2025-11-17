while True:
    editor = input("Editor: ").lower()

    if editor == "Visual Studio Code".lower():
        print("an excellent choice!")
        break

    if editor == "Word".lower() or editor == "Notepad".lower():
        print("awful")
    else:
        print("not good")
