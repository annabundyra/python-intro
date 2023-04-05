
price = input("What is the burger price? ")
price = float(price)

if(price > 20):
    price = price - 0.1 * price
    print("Discount included. Burger costs {}".format(price))
else:
    print("No discount. Burger costs {}".format(price))