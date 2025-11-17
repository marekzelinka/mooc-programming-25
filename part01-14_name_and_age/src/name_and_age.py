name = input("What is your name? ")
year_born = int(input("Which year were you born? "))

selected_year = 2021
age_in_selected_year = selected_year - year_born

print(
    f"Hi {name}, you will be {age_in_selected_year} years old at the end of the year {selected_year}"
)
