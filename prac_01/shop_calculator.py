number = int(input("Number of items: "))
total = 0
for i in range(0, number):
    price = int(input("Price of item: "))
    total = total + price
    if total > 100:
        total = total * 0.9
    else:
        total = total
print("Total price for", number, "items is:", total)
