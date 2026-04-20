"""
Defines Account base class and SavingsAccount / CurrentAccount subclasses.
"""
import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from datetime import datetime
from typing import List
from src.models.transaction import Transaction
from configuration.logger_configuration import setup_logger

logger = setup_logger("account.log")


class Account:
    def __init__(self, account_number: str, open_date: datetime):
        self.__accountNumber = account_number
        self.__openDate = open_date
        self.__balance = 0.0
        self.__transactions: List[Transaction] = []

    # Getters
    def get_account_number(self):
        return self.__accountNumber

    def get_balance(self):
        return self.__balance

    def get_open_date(self):
        return self.__openDate

    def get_transactions(self):
        return self.__transactions

    # Business logic
    def deposit(self, amount: float):
        if amount <= 0:
            logger.error(f"Attempted to deposit non-positive amount: {amount}")
            raise ValueError("Deposit amount must be positive")
        self.__balance += amount
        logger.info(f"Deposited {amount:.2f} to account {self.__accountNumber}. New balance: {self.__balance:.2f}")
        self.__transactions.append(Transaction(amount, "DEPOSIT"))

    def withdraw(self, amount: float):
        if amount <= 0:
            logger.error(f"Attempted to withdraw non-positive amount: {amount}")
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.__balance:
            logger.error(f"Attempted to withdraw amount {amount} which exceeds balance {self.__balance}")
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        logger.info(f"Withdrew {amount:.2f} from account {self.__accountNumber}. New balance: {self.__balance:.2f}")
        self.__transactions.append(Transaction(amount, "WITHDRAW"))


class SavingsAccount(Account):
    def __init__(self, account_number: str, open_date: datetime, interest_rate: float):
        super().__init__(account_number, open_date)
        self.__interestRate = interest_rate

    def get_interest_rate(self):
        return self.__interestRate


class CurrentAccount(Account):
    def __init__(self, account_number: str, open_date: datetime, overdraft_limit: float):
        super().__init__(account_number, open_date)
        self.__overdraftLimit = overdraft_limit

    def get_overdraft_limit(self):
        return self.__overdraftLimit