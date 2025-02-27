menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def addFood(item,price):
    item = input("Please add a new item onto the menu ")
    price = input("Please set a price for this new item")
    menu[item] = price
    print(menu)

addFood(1,2)
