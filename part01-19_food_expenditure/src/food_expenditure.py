days_in_week = 7

lunch_count = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery_weekly_cost = float(
    input("How much money do you spend on groceries in a week? ")
)

weekly_average_food_cost = grocery_weekly_cost + lunch_count * lunch_price
daily_average_food_cost = weekly_average_food_cost / days_in_week

print("Average food expenditure:")
print(f"Daily: {daily_average_food_cost} euros")
print(f"Weekly: {grocery_weekly_cost + lunch_count * lunch_price} euros")
