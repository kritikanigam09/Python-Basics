prices = {
    "bananas":4,
    "apple":2,
    "orange":1.5,
    "pear":3
}

stock = {
    "bananas": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices:
    print(key)
    print("price: %s"%prices[key])
    print("stock: %s"%stock[key])

    total = 0

    for key in prices:
        value = prices[key]*stock[key]
        print(value)
        total = total + value
print(total)

