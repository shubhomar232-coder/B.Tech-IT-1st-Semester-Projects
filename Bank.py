def bank_main():
    pin = ["1111", "2222", "3333", "4444", "5555"] #data of the account holders
    account_Holders_Name = ["freya", "mohak", "rajesh", "dwivedi", "god"]
    account_Number = ['223212', '299289', "332838", "335597", "447432"]
    balance = [10000, 20000, 30000, 90000, 40000]

    flag = False
    for i in range (0,999999999): #so the loop runs many times
        print("""
    \t\t\t=== Welcome To Simple BANKING System ===
""")
        inputName = input("Enter Your Name: ")
        inputName = inputName.lower()
        inputPin = 0000 #if pin is wrong it will be use as this is assigned before referance.
        index = 0 #if pin is wrong it will be use as this is assigned before referance.
        count = 0
        for name in account_Holders_Name:
            
            if name == inputName:
                index = count #index of name is stored and if the pin of that index is same user will be given access to the account.
                inputPin = input("\nEnter Pin Number: ")
            count += 1

        if inputPin == pin[index]:
            flag = True
        else:
            print("Invalid data.")
            flag = False
            continue
        if flag == True:
            print("\nYour account number is: ",account_Number[index])
            print("Your account balance is: Rs.", balance[index])
            drawOrDeposite = input("\nDo you want to draw or deposit cash (draw/deposite/no): ")
            if drawOrDeposite == "draw":
                amount = input("\nEnter the amount you want to draw: ")
                try: #Exception handling
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] - amount #subtracting the drawed amount.
                balance.remove(balance[index]) #removing the old ammount from the list and adding the new list after draw.
                balance.insert(index,remainingBalalnce)
                availableBalance = print("\nYour available balance is: ",remainingBalalnce)
            elif drawOrDeposite == "deposite":
                amount = input("Enter the amount you want to deposite: ")
                try:
                    amount = int(amount)
                    if amount > balance[index]:
                        raise
                except:
                    print("invalid amount.")
                    continue
                remainingBalalnce = balance[index] + amount #adding the deposited amount.
                balance.remove(balance[index])#removing the old ammount from the list and adding the new list after draw.
                balance.insert(index,remainingBalalnce)
                availableBalance = print("Your available balance is: ",remainingBalalnce)
            print("\nThank you for using this Simple BANKING System")

bank_main()




