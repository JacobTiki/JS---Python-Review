groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    grocery = input("Which grocery do you want to remove? ")
    if(grocery == "stop"):
        break
    groceries.remove(grocery)
    print(groceries)
    