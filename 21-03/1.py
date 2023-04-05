

def add_vat(vat, prices):

    new_prices = [(price / 100) * vat + price for price in prices]
    return new_prices

print(add_vat(vat = 20, prices = [24, 0.15, "10", 32.45]))
