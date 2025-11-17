password = input("Password: ")

while True:
    confirm_password = input("Repeat password: ")

    if confirm_password == password:
        print("User account created!")
        break

    print("They do not match!")
