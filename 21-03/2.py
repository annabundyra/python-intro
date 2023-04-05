
def apply_discount(product, discount):
    price = round(product['price'] * (1 - (discount / 100)), 2)
    assert 0 <= price <= product['price']
    return price

trainers = {'name': 'Running Trainers', 'price': 79.99}
discount = 25
print(apply_discount(trainers, discount))

trainers = {'name': 'Running Trainers', 'price': 79.99}
discount = 200
print(apply_discount(trainers, discount))



