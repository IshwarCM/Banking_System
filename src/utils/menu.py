"""
Menu/controller layer for user actions.
"""
import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.models.account import Account
from src.models.transaction import Transaction

class Menu:
    def __init__(self, customer_store, account_store, transaction_store):
        self.__customer_store = customer_store
        self.__account_store = account_store
        self.__transaction_store = transaction_store
        self.__logged_in_customer = None

    # ---------- AUTH ---------- #
    def login(self, email, password):
        customer = self.__customer_store.authenticate(email, password)
        if not customer:
            return False
        self.__logged_in_customer = customer
        return True

    def logout(self):
        self.__logged_in_customer = None

    def get_logged_in_customer(self):
        if not self.__logged_in_customer:
            raise PermissionError("Not logged in")
        return self.__logged_in_customer

    # ---------- CUSTOMER ---------- #
    def register_customer(self, customer):
        self.__customer_store.add_customer(customer)

    # ---------- ACCOUNT ---------- #
    def open_account(self, account):
        self.get_logged_in_customer().add_account(account)
        self.__account_store.add_account(account)

    def get_account(self, acc_no):
        account = self.__account_store.find_by_account_number(acc_no)
        if not account:
            raise ValueError("Account not found")
        return account

    # ---------- TRANSACTION ---------- #
    def deposit(self, account, amount):
        account.deposit(amount)
        self.__transaction_store.add_transaction(account.get_transactions()[-1])

    def withdraw(self, account, amount):
        account.withdraw(amount)
        self.__transaction_store.add_transaction(account.get_transactions()[-1])

    def show_account_transactions(self, account):
        return account.get_transactions()