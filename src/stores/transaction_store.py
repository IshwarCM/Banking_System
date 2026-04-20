import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.transaction import Transaction
from configuration.logger_configuration import setup_logger

logger = setup_logger("transaction_store.log")

class TransactionStore:
    def __init__(self):
        self.__transactions: List[Transaction] = []

    def add_transaction(self, transaction: Transaction):
        logger.info(f"Adding transaction to transaction store")
        self.__transactions.append(transaction)

    def get_all_transactions(self):
        logger.info(f"Retrieving all transactions from transaction store")
        return self.__transactions