from decimal import Decimal, ROUND_HALF_EVEN
import time

class BankAccount:
    """The blueprint for creating digital bank accounts. Acts as a container for data (Owner, Balance) and defines actions (Deposit, Withdraw, Check Balance) that can be performed on that data"""
    
    def __init__(self,owner,balance):
        
        if not isinstance(owner,str):
            raise ValueError(f'Owner parameter must be a string. Got {owner}, which is {type(owner).__name__}.')
        if not owner:
            raise ValueError(f'Owner parameter cannot be an empty string. Got ("",{balance}).')
        
        balance = self._get_decimal(balance)
        if balance < 0:
            raise ValueError(f'Expected positive balance, got {balance}')
        
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self,amount):
        """Instance method to add money to the bank account."""
        amount = self._get_decimal(amount)
        if amount <= 0:
            raise ValueError(f'Expected positive amount, got {amount}')
        self.balance += amount
        self._log_transaction('deposit',amount)
    
    def withdraw(self,amount):
        """Instance method to withdraw money from the bank account."""
        amount = self._get_decimal(amount)
        if amount <= 0:
            raise ValueError(f'Expected positive amount, got {amount}')
        if amount > self.balance:
            raise ValueError(f'Withdraw amount cannot exceed balance. Current balance: {self.balance}, got {amount}')
        self.balance -= amount
        self._log_transaction('withdraw',amount)
    
    def get_balance(self):
        """Instance method to get the amount of money in the bank account"""
        return self.balance
    
    def get_history(self):
        """Instance method to get the history of transactions of the bank account"""
        return self.history
    
    def _log_transaction(self,transaction,amount):
        """Helper method to log the transaction made in the history list"""
        self.history.append({"transaction":transaction,"amount":amount,"timestamp":time.time()})
    
    def _get_decimal(self,amount):
        """Helper method to get the decimal version of the numeric input given"""
        self._validate_numeric_input(amount)
        str_amount = str(amount)
        decimal_amount = Decimal(str_amount).quantize(Decimal('0.00'),rounding=ROUND_HALF_EVEN)
        return decimal_amount
        
    def _validate_numeric_input(self,amount):
        """Helper method to validate if the numeric input is a numeric string, an integer, or a float."""
        if isinstance(amount,str):
            if amount.isnumeric():
                return True
            raise ValueError(f'String must be numeric, got "{amount}"')
        if isinstance(amount,int) or isinstance(amount,float):
            return True
        raise TypeError(f'Expected numeric str, int, or float, got {type(amount).__name__}.')