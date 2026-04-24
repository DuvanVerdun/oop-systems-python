class BankAccount:
    """The blueprint for creating digital bank accounts. Acts as a container for data (Owner, Balance) and defines actions (Deposit, Withdraw, Check Balance) that can be performed on that data"""
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amount):
        """Instance method to add money to the bank account."""
        if amount <= 0:
            return "Deposit amount must be positive."
        total = self.balance + amount
        return f"You have deposited {amount}. Now you have {total} in your bank account"
    
    def withdraw(self,amount):
        """Instance method to withdraw money from the bank account."""
        if amount > self.balance:
            return f"Insufficent funds. Current Balance: {self.balance}"
        total = self.balance - amount
        return f"You have withdrawn {amount}. Now you have {total} in your bank account"
    
    def check_balance(self):
        """Instance method to show the amount of money in the bank account"""
        return f"Hello {self.owner}. You have {self.balance} in your bank account"