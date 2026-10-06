
# ATM in python

def require_amount():
    while True:
        try:
            amount = int(input("Enter an amount: "))
            if amount <= 0:
                print("Enter a valid amount: ")
            else:
                return amount
        except ValueError:
            print("Insert valid amount ")    

def deposit(amount):
        money = require_amount()
        amount += money 
        print("Amount deposited successfully ") 
        return amount

def withdraw(amount):
        remove = require_amount()
        if remove > amount:
            print("Insufficient funds")
            return amount  
        else:
            amount -= remove
            print("Amount successfully withdraw ")
            return amount      
            
amount = 1000

while True:
    print("\n = MENU = ")
    print("1) Show amount ")
    print("2) Deposit amount ")
    print("3) Withdraw amount ") 
    print("4) Exit of the program ")
    try:
        choice = int(input("Select an option: (1 - 4)"))
        match choice:
            case 1:
                print("================")
                print(f"Actual amount: ${amount}")
                print("================")
            
            case 2:
                print("================")
                amount = deposit(amount)
                print("================")
                
            case 3:
                print("================") 
                amount = withdraw(amount)
                print("================") 
            
            case 4:
                print("Exiting . . . ")   
                break
            
            case _:
                print("Invalid option")
    except ValueError:
        print("Insert a valid option ")            
                  
    
                    
