import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.account import Account


class AccountStore:
    def __init__(self):
        self.__accounts: List[Account] = []

    def add_account(self, account: Account):
        self.__accounts.append(account)

    def remove_account(self, account: Account):
        self.__accounts.remove(account)

    def get_all_accounts(self):
        return self.__accounts

    def find_by_account_number(self, account_number: str):
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        return None