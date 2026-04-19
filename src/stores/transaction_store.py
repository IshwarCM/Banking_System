import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.transaction import Transaction


class TransactionStore:
    def __init__(self):
        self.__transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        self.__transactions.append(transaction)

    def get_all_transactions(self):
        return self.__transactions