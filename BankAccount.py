class BankAccount:
  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdrawal(self, amount):
    self.balance -= amount

  def display_balance(self):
    print(f"Your balance is: ${self.balance}")