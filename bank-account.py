class BankAccount:
    """The blueprint for creating digital bank accounts. Acts as a container for data (Owner, Balance) and defines actions (Deposit, Withdraw, Check Balance) that can be performed on that data"""
    
    def __init__(self,owner,balance):
        if not owner:
            raise ValueError("Owner cannot be empty")
        if not isinstance(balance,int):
            raise TypeError(f"Balance must be an integer, got {type(balance).__name__}")
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        
        self.owner = owner
        self.balance = balance
        
        self.history = []
    
    def deposit(self,amount):
        """Instance method to add money to the bank account."""
        if not isinstance(amount,int):
            raise TypeError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        self.balance += amount
        self._log_transaction("deposit",amount)
    
    def withdraw(self,amount):
        """Instance method to withdraw money from the bank account."""
        if not isinstance(amount,int):
            raise TypeError("Amount must be an integer")
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if amount > self.balance:
            raise ValueError("Withdraw amount cannot exceed balance value.")
        self.balance -= amount
        self._log_transaction("withdraw",amount)
    
    def check_balance(self):
        """Instance method to show the amount of money in the bank account"""
        return self.balance
    
    def check_history(self):
        """Instance method to show the history of transactions of the bank account"""
        return self.history
    
    def _log_transaction(self,transaction,amount):
        """Helper method to log the transaction made in the history list"""
        if transaction == "deposit":
            transaction += "ed"
        else:
            transaction += "n"
        self.history += [f"{transaction}: {amount}"]