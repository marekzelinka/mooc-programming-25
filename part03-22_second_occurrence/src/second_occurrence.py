string = input("Please type in a string: ")
query = input("Please type in a substring: ")

first_start_index = string.find(query)
first_end_index = first_start_index + len(query)

second_start_index = -1

if first_start_index != -1:
    string = string[first_end_index:]
    second_start_index = string.find(query)

if second_start_index == -1:
    print("The substring does not occur twice in the string.")
else:
    print(
        f"The second occurrence of the substring is at index {first_end_index + second_start_index}."
    )
