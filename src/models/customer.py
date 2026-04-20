"""
Defines Customer, Individual, and Corporate classes.
"""

import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)
    
from datetime import date
from typing import List
from src.models.account import Account
from configuration.logger_configuration import setup_logger

logger = setup_logger("customer.log")

class Customer:
    __total_customers = 0

    def __init__(self, name, address, contact_number, email, password):
        self.__name = name
        self.__address = address
        self.__contactNumber = contact_number
        self.__email = email
        self.__password = password
        self.__accounts: List[Account] = []

        Customer.__total_customers += 1

    # Authentication helpers
    def check_credentials(self, email, password):
        result = self.__email == email and self.__password == password
        if not result:
            logger.warning(f"Failed login attempt for email: {email}")
        else:
            logger.info(f"Checking credentials for email: {email}")
        return result

    # Account management
    def add_account(self, account: Account):
        logger.info(f"Adding account with account number {account.get_account_number()} to customer {self.__name}")
        self.__accounts.append(account)

    def get_accounts(self):
        return self.__accounts

    # Profile management
    def get_name(self):
        return self.__name

    def set_address(self, address):
        self.__address = address
        logger.info(f"Updated address for customer {self.__name}")

    def set_contact_number(self, number):
        self.__contactNumber = number
        logger.info(f"Updated contact number for customer {self.__name}")

    def set_email(self, email):
        self.__email = email
        logger.info(f"Updated email for customer {self.__name}")

    @classmethod
    def totalNumberOfCustomers(cls):
        return cls.__total_customers


class Individual(Customer):
    def __init__(
        self,
        name,
        address,
        contact_number,
        email,
        password,
        surname,
        gender,
        dob: date
    ):
        super().__init__(name, address, contact_number, email, password)
        self.__surname = surname
        self.__gender = gender
        self.__dateOfBirth = dob

    def workOutAge(self):
        today = date.today()
        return today.year - self.__dateOfBirth.year


class Corporate(Customer):
    def __init__(
        self,
        name,
        address,
        contact_number,
        email,
        password,
        company_type
    ):
        super().__init__(name, address, contact_number, email, password)
        self.__companyType = company_type