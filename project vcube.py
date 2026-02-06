inventory = ['milk','curd','apple','banana','orange','pineapple','strawberry']
prices = [70,90,60,50,45,90,130]
quantities = [1,1,1,1,1,500,1]
cart = []
total_revenue = 0
print("INVENTORY MANAGEMENT")
print("1.owner")
print("2.user")
print("Select Your Role")
choice = int(input('Enter your option'))
if choice == 1:
    while True:
        print('select option')
        print('1.add items ')
        print('2.remove item')
        print('3.update item')
        print('4.view inventory')
        print('5.Exit')
        oc = int(input('Enter your option'))
        if oc == 1:
            name = input('Enter item name:')
            price = int(input('Enter price of the item:'))
            quantity = int(input('Enter quantity:'))
            if name in inventory:
                print('Item already exists')
            else:
                inventory.append(name)
                prices.append(price)
                quantities.append(quantity)
                print('items added successfully')
        elif oc == 2:
            name = input(' remove items : ')
            if name in inventory:
                i = inventory.index(name)
                inventory.pop(i)
                prices.pop(i)
                quantities.pop(i)
                print(' Items removed successfully')
            else:
                print('item not found')
        elif oc == 3:
            name = input('Enter item to update:')
            if name in inventory:
                i = inventory.index(name)
                print('1. update price')
                print('2. update quantity')
                ch = int(input('enter choice:'))
                if ch == 1:
                        prices[i] = int(input('Enter new price:'))
                        print('price updated successfully')
                if ch == 2:
                        quantities[i] = int(input('Enter new quantity:'))
                        print('quantity updated successfully')
            else:
                print('Item not found')
        elif oc == 4:
            print('Inventory    prices    quantities')
            print('---------------------------------')
            for i in range (len(inventory)):
                print(inventory[i], " " , prices[i], " " , quantities[i])
        elif oc == 5:
            break
if choice == 2:
     name = input('Enter your name:')
     number = int(input('Enter your number:'))
     while True:
         print('user menu')
         print('1.add to cart')
         print('2.remove from cart')
         print('4.view cart')
         print('5.billing')
         print('6.Exit')
         uc = int(input('Enter your choice:'))
         if uc == 1:
             for i in range (len(inventory)):
                print(inventory[i], " " , prices[i], " " , quantities[i])
             item = input('Enter your item from inventory to add in cart:')
             if item in inventory:
                 i = inventory.index(item)
                 if quantities[i] > 0:
                     cart.append(item)
                     quantities[i] -=  1
                     print('Items added to cart successfully')
                 else:
                     print('out of stock')
             else:
                print('Item not found')
         elif uc == 2:
             print('cart:', cart)
             name = input('Enter item to removed from cart:')
             if name in cart:
                 cart.remove(name)
                 i = inventory.index(name)
                 quantities[i] +=  1
                 print('Items removed from cart')
             else:
                 print('Item not found in cart')
         elif uc == 3:
             total = 0
             for item in cart:
                 i = inventory.index(item)
                 print(item, "-", prices[i])
                 total = total + prices[i]
             print('total bill is:',total)
         elif uc == 4:
           bill = 0
           for item in cart:
               i = inventory.index(item)
               bill = bill + prices[i]
               print('final bill amount:',bill)
               total_revenue = total_revenue + bill
               cart.clear()
         elif uc == 5:
             break
else:
    print('invalid option')
                
