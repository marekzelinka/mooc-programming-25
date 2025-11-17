while True:
    editor = input("Editor: ").lower()

    if editor == "visual studio code":
        print("an excellent choice!")
        break

    if editor == "word" or editor == "notepad":
        print("awful")
    else:
        print("not good")
