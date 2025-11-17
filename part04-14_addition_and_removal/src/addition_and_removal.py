from typing import List

list: List[int] = []


while True:
    print(f"The list is now {list}")

    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == "d":
        list.append(len(list) + 1)
    elif action == "r":
        if len(list) != 0:
            list.pop()
    elif action == "x":
        print("Bye!")

        break
