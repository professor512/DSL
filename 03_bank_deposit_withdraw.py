def deposit(num):
    global balance
    balance += num
    
def withdrawal(num):
    global balance
    if balance >= num:
        balance -= num
    else:
        print("Withdrawal not possible because balance is insufficient.")
        
balance = 0


while True:
    data = input("Please enter the transaction details (or type 'Exit' to end): ")
    
    if data.lower() == 'exit':
        break
    try:
        action, amount_str = data.split()
        amount = int(amount_str)
        
        if action.upper() == 'D':
            deposit(amount)
        elif action.upper() == 'W':
            withdrawal(amount)
        else:
            print("Invalid transaction type. Use 'D' for deposit and 'W' for withdrawal.")
        print("Balance =", balance)
    
    except ValueError:
        print("Invalid input format. Please enter in the format 'D amount' or 'W amount'.")
