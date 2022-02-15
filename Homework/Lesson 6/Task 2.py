prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for food in prices:
    print(food.title())
    print("Price: ", prices[food])
    print("Stock: ", stock[food])
    print("Total price: ", prices[food]*stock[food] )


