attempts = 1

while True:
    code = input("PIN: ")

    if code == "4321":
        break

    print("Wrong")
    attempts += 1

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
