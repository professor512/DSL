# Write a Python program that computes the net amount of a bank account based a 
# transaction log from console input. The transaction log format is shown as 
# following: D 100 W 200 (Withdrawal is not allowed if balance is going negative. 
# Write functions for withdraw and deposit) D means deposit while W means 
# withdrawal. Suppose the following input is supplied to the program:
# D 300, D 300 , W 200, D 100 Then, the output should be: 500

def deposit(amount):
    global balance
    balance += amount

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance to withdraw")
    else:
        balance -= amount

balance = 0 

while True:
    data = input("\nEnter Transaction Details: ")
    
    action, amount = data.split()
    amount = int(amount)
    if action.upper() == 'D':
        deposit(amount)
    elif action.upper() == 'W':
        withdraw(amount)
    else:
        print("\nInvalid Input Format")
    print("\nTotal In Bank", balance)
