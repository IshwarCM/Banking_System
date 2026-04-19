"""
Defines the ABCBankingGroup class.
"""

import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.customer import Customer
from src.models.account import Account


class ABCBankingGroup:
    def __init__(self):
        self.__customers: List[Customer] = []
        self.__accounts: List[Account] = []

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def get_customers(self):
        return self.__customers

    def get_all_accounts(self):
        return self.__accounts