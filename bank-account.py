import re
from decimal import Decimal,InvalidOperation, ROUND_HALF_EVEN
from datetime import datetime
import uuid
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    REVERSAL = "reversal"

class BankAccount:
    """The blueprint for creating digital bank accounts. Acts as a container for data (Owner, Balance, History of Transactions) and defines actions (Deposit, Withdraw, Get Balance, Get History) that can be performed on that data"""
    
    MIN_BALANCE = Decimal('25.00')
    DAILY_LIMIT = Decimal('1000.00')
    
    def __init__(self,owner,balance):
        
        if not isinstance(owner,str):
            raise ValueError(f'Owner parameter must be a string. Got {owner}, which is {type(owner).__name__}.')
        if not owner:
            raise ValueError(f'Owner parameter cannot be an empty string. Got ("",{balance}).')
        
        balance = self._convert_to_decimal(balance)
        if balance < 0:
            raise ValueError(f'Expected positive balance, got {balance}')
        
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self,amount):
        """Instance method to add money to the bank account."""
        amount = self._convert_to_decimal(amount)
        if amount <= 0:
            raise ValueError(f'Deposit amount must be positive, got {amount} as the amount value')
        self.balance += amount
        self._log_transaction(TransactionType.DEPOSIT,amount)
    
    def withdraw(self,amount):
        """Instance method to withdraw money from the bank account."""
        amount = self._convert_to_decimal(amount)
        if amount <= 0:
            raise ValueError(f'Withdraw amount must be positive, got {amount} as the amount value')
        if amount > self.balance:
            raise ValueError(f'Withdraw amount cannot exceed balance. Current balance: {self.balance}, got {amount}')
        today_total = self._get_today_total_withdrawn()
        if today_total+amount > self.DAILY_LIMIT:
            raise ValueError(f"Transaction declined: Daily withdrawal limit of {str(self.DAILY_LIMIT)} exceeded.")
        if self.balance - amount < self.MIN_BALANCE:
            raise ValueError(f"Transaction declined: Maintaining a minimum balance of {str(self.MIN_BALANCE)} is required.")
        self.balance -= amount
        self._log_transaction(TransactionType.WITHDRAW,amount)
        
    def reversal(self,target_id):
        """Instance method to reversal a transaction made in the bank account"""
        transaction_type,amount = "",""
        for t in self.history:
            if t["ID"] == target_id:
                transaction_type,amount = t["transaction"],t["amount"]
        if not transaction_type:
            raise ValueError(f"target_id must be in history dictionary. Got {target_id}, which was not found.")
        if any(transaction["reference_ID"] == target_id for transaction in self.history):
            raise ValueError(f"Transaction {target_id} has already been reversed. A transaction can only be reversed once to maintain balance integrity.")
        if transaction_type == TransactionType.DEPOSIT.value:
            self.balance -= Decimal(amount)
            self._log_transaction(TransactionType.REVERSAL,amount,target_id)
        if transaction_type == TransactionType.WITHDRAW.value:
            self.balance += Decimal(amount)
            self._log_transaction(TransactionType.REVERSAL,amount,target_id)
    
    def get_balance(self):
        """Instance method to get the amount of money in the bank account"""
        return self.balance
    
    def get_history(self,transaction_filter=None):
        """Instance method to get the history of transactions of the bank account"""
        if transaction_filter and transaction_filter not in [type.value for type in TransactionType]:
            raise ValueError(f"transaction_filter does not match any transaction type. Got '{transaction_filter}'. Expected: '{TransactionType.DEPOSIT.value}' or '{TransactionType.WITHDRAW.value}' or '{TransactionType.REVERSAL.value}'")
        history_copy = [t.copy() for t in self.history if not transaction_filter or transaction_filter == t["transaction"]]
        return history_copy
    
    def _log_transaction(self,transaction,amount,reference_id=None):
        """Helper method to log the transaction made in the history list"""
        now = datetime.now()
        unique_id = uuid.uuid4()
        self.history.append({"index":len(self.history)+1,"transaction":transaction.value,"amount":amount,"resulting_balance":Decimal(self.balance),"timestamp":now.strftime("%d/%m/%y %I:%M %p"),"raw_timestamp":now,"ID":unique_id.hex,"reference_ID":reference_id})
    
    def _convert_to_decimal(self,amount):
        """Helper method to get the decimal version of the numeric input given"""
        try:
            return Decimal(amount).quantize(Decimal('0.00'),rounding=ROUND_HALF_EVEN)
        except (InvalidOperation,TypeError):
            raise InvalidOperation(f"Conversion failed for: '{amount}' (type: {type(amount).__name__}). Expected numeric string or integer.")
        
    def _get_today_total_withdrawn(self):
        """Helper method to get the information of how much did the owner has withdrawn from his bank account today"""
        total = Decimal('0.00')
        reversals = Decimal('0.00')
        today = datetime.now().date()
        for t in self.history:
            transaction_date = t["raw_timestamp"]
            if transaction_date.date() == today:
                if t["transaction"] == TransactionType.WITHDRAW.value:
                    total += Decimal(t["amount"])
                if t["transaction"] == TransactionType.REVERSAL.value:
                    reference_id = t["reference_ID"]
                    original_t = next((transaction for transaction in self.history if transaction["ID"] == reference_id),None)
                    if original_t and original_t["transaction"] == TransactionType.WITHDRAW.value:
                        if original_t["raw_timestamp"].date() == today:
                            reversals += t["amount"]
        return total - reversals