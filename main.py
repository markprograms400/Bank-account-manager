from BankAccount import BankAccount 

account_holder = input("What is your name: ")
balance = float(input("What is your starting balance: "))

account = BankAccount(account_holder, balance)


while True: 
  print("""
  Welcome to your Account: 
  1. Deposit 
  2. Withdrawal
  3. Display your balance
  4. Exit""")
  
  
  choice = int(input("Choose your option (1-4): "))

  if choice == 1:
    amount = int(input("How much would you like to deposit: "))
    account.deposit(amount)
    print(f"{account_holder}, You have deposited {amount} to your account.")

  elif choice == 2:
    amount = int(input("How much would you like to withdrawal: "))
    account.withdrawal(amount)
    print(f"{account_holder}, You have withdrawn {amount} from your account.")

  elif choice == 3:
    account.display_balance()

  elif choice == 4: 
    print(f"Thank you {account_holder} for using our service.")
    break

  else: 
    print("Invalid choice, try again: ")