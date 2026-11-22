price_input, discount_input =\
    float(input("Enter the price of a good: ")), int(input("Enter the discount of a good: "))
if discount_input <= 0 or discount_input > 100:
    print("Invalid discount value")
    exit()

discount = discount_input/100
new_price = price_input * discount

print(round(price_input - new_price, 2))