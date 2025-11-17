limit = int(input("Limit: "))

consecutive_sum = 1
step = 1
calculation = "1"

while consecutive_sum < limit:
    step += 1
    consecutive_sum += step
    calculation += f" + {step}"

print(f"The consecutive sum: {calculation} = {consecutive_sum}")
