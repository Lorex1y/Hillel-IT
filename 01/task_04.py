price_input, discount_input =\
    int(input("Enter the price of a good: ")), int(input("Enter the discount of a good: "))
if discount_input <= 0 or discount_input > 100:
    print("Invalid discount value")
    exit()

discount = discount_input/100
new_price = price_input * discount

print(price_input - new_price)