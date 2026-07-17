print("============================================================================================================================================")
print("----------------------------------------------------------------------------------------GENERALSTORE-------------------------------------------------------------------------------------------------------")
print("============================================================================================================================================")
print("ENTER [H] BELOW")

products = {"apple": {"price": 30, "stock": 50},    
                        "banana":{"price": 10, "stock": 100},
                        "milk":{"price": 25, "stock": 20},
                        "bread":{"price": 20, "stock": 15},
                        "eggs":{"price": 5, "stock": 60},
                        "juice":{"price": 40, "stock": 55},
                        "soap":{"price": 15, "stock": 80}}
cart = {}
shop_open = True

while shop_open:
    command = input("\nWhat would you like to do now? ").lower()
    if command == "h":
        print("---------------------[H] FOR HELP------------------")
        print("--------------[SC] FOR STOCK CHECK---------")
        print("---------------[SP] FOR STOCK PRICE----------")
        print("---------------------[S] FOR SHOP------------------")
        print("------------------[A] FOR ADDDING---------------")
        print("------[C] FOR VIEWING ITEMS IN CART-----")
        print("--------[P] FOR PURCHASING ITEMS---==--")
        print("------------------[E] FOR EXITING-----------------")

    elif command =="sc":
        print("\n STOCK ITEMS:")
        for item in products:
            print(item.title(), "-", products[item]["stock"], "left")

    elif command=="sp":
        print("\nPrices of products:")
        for item in products:
            print(item.title(), "-", products[item]["price"])

    elif command == "shop" or command == "s":
        print("\nYou can buy the following items:")
        for item in products:
            print("-", item)

    elif command == "add to cart" or command == "a":
        item = input("Which item do you want to add? ").lower()
        if item in products:
            qty = int(input("How many do you want to add? "))
            if qty <= products[item]["stock"]:
                products[item]["stock"] -= qty
                if item in cart:
                    cart[item] += qty
                else:
                    cart[item] = qty
                print(qty, item, "added to your cart.")
            else:
                print("Sorry, we don't have that many in stock.")
        else:
            print("That item is not available in our shop.")

    elif command == "cart" or command == "c":
        print("\nHere's what you have in your cart:")
        total = 0
        if cart == {}:
            print("Your cart is empty.")
        else:
            print("Item        Qty     Total")
            for item in cart:
                qty = cart[item]
                price = products[item]["price"]
                total_price = qty * price
                total += total_price
                print(f"{item:10}  {qty:<5}   {total_price}")
            print("Total amount: ", total)

    elif command == "purchase" or command == "p":
        print("\n********* BILL ********")
        if cart == {}:
            print("Your cart is empty. Nothing to purchase.")
        else:
            total = 0
            print("Item        Qty   Price   Total")
            print("-------------------------------")
            for item in cart:
                qty = cart[item]
                rate = products[item]["price"]
                total_item = qty * rate
                total += total_item
                print(f"{item:10} {qty:<5} {rate:<6} {total_item}")
            print("-------------------------------")
            print("Grand Total: ", total)
            print("Thanks for shopping with us!")
            cart = {}

    elif command == "exit" or command == "e":
        print("\nThanks for visiting SHUBH GROCERY SHOP. Have a nice day!")
        shop_open = False

    else:
        print("Sorry, I didn t get that. Type 'help' if you re stuck.")
