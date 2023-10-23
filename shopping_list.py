# Create a program for customers to choose their desired items based on number ids and at the end of the end of the program, let them know what the total cost is
itemId = list()
total = list()
goodPrice = {
    "item1": {"10.0": 5.50},
    "item2": {"11.1": 1.99},
    "item3": {"20.3": 35.00},
    "item4": {"6.4": 26.52}
    }

# a list of the item ids
itemValues = [itemID for (a, itemID) in goodPrice.items()]
for x in itemValues:
    for (y, z) in x.items():
        itemId.append(y)

# ask the user to enter the item and the desired amount, do this until done
reply = ''
while reply != 'done':

    userSelect = input(f"Enter 1, 2, 3, 4 for item 1 - 4 respectively: ")
    # error check
    try:
        userSelect = int(userSelect)
    except:
        print("Enter the digits specified only!")
        continue

    #check the item price
    indexId = userSelect - 1
    try:
        idSelect = itemId[indexId]
    except:
        print(f"item {userSelect} is not available at the moment.")
        continue
    itemPrice = itemValues[indexId][idSelect]
    print(f"The price of the selected item is {itemPrice}.")

    # get the number of desired items
    def getCount():
        countSelect = None
        while countSelect is None:
            countSelect = input("How many of these do you want: ")
            try:
                countSelect = int(countSelect)
            except:
                print("Enter numeric values only!")
                continue
        
        return countSelect
    
    count = getCount()
    try:
        total.append(itemPrice*count)
    except:
        print("couldn't add to cart")
        continue

    # check to see if the customer wants to continue
    reply = input("Would you like to continue? if yes \'y\', if no enter \'done\':  ").lower()
    if reply == 'y':
        continue

# output the total items with their prices
print(f"The total price is {sum(total):.2f}")

    
    

        