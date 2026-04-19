import os 
import sys 

# add project root to python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from typing import List
from src.models.customer import Customer


class CustomerStore:
    def __init__(self):
        self.__customers: List[Customer] = []

    def add_customer(self, customer: Customer):
        self.__customers.append(customer)

    def remove_customer(self, customer: Customer):
        self.__customers.remove(customer)

    def get_all_customers(self):
        return self.__customers

    def find_by_email(self, email: str):
        for customer in self.__customers:
            if customer._Customer__email == email:
                return customer
        return None

    def authenticate(self, email, password):
        for customer in self.__customers:
            if customer.check_credentials(email, password):
                return customer
        return None