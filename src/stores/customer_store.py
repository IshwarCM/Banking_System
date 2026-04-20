import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.customer import Customer
from configuration.logger_configuration import setup_logger

logger = setup_logger("customer_store.log")

class CustomerStore:
    def __init__(self):
        self.__customers: List[Customer] = []

    def add_customer(self, customer: Customer):
        logger.info(f"Adding customer {customer.get_name()} with email {customer.get_email()} to customer store")
        self.__customers.append(customer)

    def remove_customer(self, customer: Customer):
        logger.info(f"Removing customer {customer.get_name()} with email {customer.get_email()} from customer store")
        self.__customers.remove(customer)

    def get_all_customers(self):
        return self.__customers

    def find_by_email(self, email: str):
        logger.info(f"Searching for customer with email {email}")
        for customer in self.__customers:
            if customer._Customer__email == email:
                logger.info(f"Customer found with email {email}")
                return customer
        logger.warning(f"Customer not found with email {email}")
        return None

    def authenticate(self, email, password):
        logger.info(f"Attempting to authenticate customer with email {email}")
        for customer in self.__customers:
            if customer.check_credentials(email, password):
                logger.info(f"Customer authenticated successfully with email {email}")
                return customer
        logger.warning(f"Authentication failed for customer with email {email}")
        return None