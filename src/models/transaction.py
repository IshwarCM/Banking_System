"""
Defines Transaction models.
"""
import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
    
from datetime import datetime
from configuration.logger_configuration import setup_logger


logger = setup_logger("transaction.log")


class Transaction:
    def __init__(self, amount: float, transaction_type: str):
        self.__amount = amount
        self.__transactionType = transaction_type
        self.__timeStamp = datetime.now()

    def get_amount(self):
        return self.__amount

    def get_type(self):
        return self.__transactionType

    def get_timestamp(self):
        return self.__timeStamp


class DirectDebit(Transaction):
    def __init__(self, amount: float, payment_date):
        super().__init__(amount, "DIRECT_DEBIT")
        self.__paymentDate = payment_date

    def get_payment_date(self):
        return self.__paymentDate


class ExternalTransaction(Transaction):
    def __init__(
        self,
        amount: float,
        branch_name: str,
        branch_address: str,
        branch_post_code: str,
        branch_code: str
    ):
        super().__init__(amount, "EXTERNAL")
        self.__branchName = branch_name
        self.__branchAddress = branch_address
        self.__branchPostCode = branch_post_code
        self.__branchCode = branch_code