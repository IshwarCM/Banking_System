import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.account import Account
from configuration.logger_configuration import setup_logger

logger = setup_logger("account_store.log")

class AccountStore:
    def __init__(self):
        self.__accounts: List[Account] = []

    def add_account(self, account: Account):
        logger.info(f"Adding account with account number {account.get_account_number()} to account store")
        self.__accounts.append(account)

    def remove_account(self, account: Account):
        logger.info(f"Removing account with account number {account.get_account_number()} from account store")
        self.__accounts.remove(account)

    def get_all_accounts(self):
        return self.__accounts

    def find_by_account_number(self, account_number: str):
        logger.info(f"Searching for account with account number {account_number}")
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                logger.info(f"Account found with account number {account_number}")
                return account
        logger.warning(f"Account not found with account number {account_number}")
        return None