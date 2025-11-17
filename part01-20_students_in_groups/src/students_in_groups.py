student_count = int(input("How many students on the course? "))
group_size = int(input("Desired group size? "))

group_count = (student_count + group_size - 1) // group_size

print(f"Number of groups formed: {group_count}")
