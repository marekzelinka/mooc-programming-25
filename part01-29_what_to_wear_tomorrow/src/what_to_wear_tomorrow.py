print("What is the weather forecast for tomorrow?")

temp_in_c = int(input("Temperature: "))
expect_rain = input("Will it rain (yes/no): ")

print("Wear jeans and a T-shirt")

if temp_in_c <= 20:
    print("I recommend a jumper as well")

if temp_in_c <= 10:
    print("Take a jacket with you")

if temp_in_c <= 5:
    print("Make it a warm coat, actually")
    print("I think gloves are in order")

if expect_rain == "yes":
    print("Don't forget your umbrella!")
