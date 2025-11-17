gift_amount = int(input("Value of gift: "))

if gift_amount < 5000:
    gift_tax = 0
elif gift_amount < 25000:
    gift_tax = 100 + (gift_amount - 5000) * 0.08
elif gift_amount < 55000:
    gift_tax = 1700 + (gift_amount - 25000) * 0.1
elif gift_amount < 200000:
    gift_tax = 4700 + (gift_amount - 55000) * 0.12
elif gift_amount < 1000000:
    gift_tax = 22100 + (gift_amount - 200000) * 0.15
else:
    gift_tax = 142100 + (gift_amount - 1000000) * 0.17

if gift_tax == 0:
    print("No tax!")
else:
    print(f"Amount of tax: {gift_tax} euros")
