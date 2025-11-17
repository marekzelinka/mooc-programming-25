limit = int(input("Limit: "))

step = 1
consecutive_sum = 1

while consecutive_sum < limit:
    step += 1
    consecutive_sum += step

print(consecutive_sum)
