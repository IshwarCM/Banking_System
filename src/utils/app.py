"""
Application entry point for Banking Management System
"""

import os
import sys
from datetime import datetime, date

# add project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

from src.models.customer import Individual, Corporate
from src.models.account import SavingsAccount, CurrentAccount
from src.stores.customer_store import CustomerStore
from src.stores.account_store import AccountStore
from src.stores.transaction_store import TransactionStore
from src.utils.menu import Menu


def print_main_menu():
    print("\n==== ABC BANKING SYSTEM ====")
    print("1. Register Customer")
    print("2. Login")
    print("3. Open Account")
    print("4. Deposit")
    print("5. Withdraw")
    print("6. Transfer Funds")
    print("7. View Accounts")
    print("8. Transaction History")
    print("9. Logout")
    print("0. Exit")


def main():
    customer_store = CustomerStore()
    account_store = AccountStore()
    transaction_store = TransactionStore()

    menu = Menu(customer_store, account_store, transaction_store)

    while True:
        print_main_menu()
        choice = input("Choose an option: ")

        try:
            # ---------------- REGISTER ---------------- #
            if choice == "1":
                cust_type = input("Individual or Corporate (I/C): ").upper()
                name = input("Name: ")
                address = input("Address: ")
                contact = input("Contact Number: ")
                email = input("Email: ")
                password = input("Password: ")

                if cust_type == "I":
                    surname = input("Surname: ")
                    gender = input("Gender: ")
                    dob = date.fromisoformat(input("DOB (YYYY-MM-DD): "))
                    customer = Individual(
                        name, address, contact, email, password,
                        surname, gender, dob
                    )
                else:
                    company_type = input("Company Type: ")
                    customer = Corporate(
                        name, address, contact, email, password, company_type
                    )

                menu.register_customer(customer)
                print("✅ Customer registered successfully")

            # ---------------- LOGIN ---------------- #
            elif choice == "2":
                email = input("Email: ")
                password = input("Password: ")
                if menu.login(email, password):
                    print("✅ Login successful")
                else:
                    print("❌ Invalid credentials")

            # ---------------- OPEN ACCOUNT ---------------- #
            elif choice == "3":
                acc_type = input("Savings or Current (S/C): ").upper()
                acc_no = input("Account Number: ")

                if acc_type == "S":
                    rate = float(input("Interest Rate: "))
                    account = SavingsAccount(acc_no, datetime.now(), rate)
                else:
                    limit = float(input("Overdraft Limit: "))
                    account = CurrentAccount(acc_no, datetime.now(), limit)

                menu.open_account(account)
                print("✅ Account opened")

            # ---------------- DEPOSIT ---------------- #
            elif choice == "4":
                acc_no = input("Account Number: ")
                amt = float(input("Amount: "))
                account = account_store.find_by_account_number(acc_no)
                menu.deposit(account, amt)
                print("✅ Deposit successful")

            # ---------------- WITHDRAW ---------------- #
            elif choice == "5":
                acc_no = input("Account Number: ")
                amt = float(input("Amount: "))
                account = account_store.find_by_account_number(acc_no)
                menu.withdraw(account, amt)
                print("✅ Withdrawal successful")

            # ---------------- TRANSFER ---------------- #
            elif choice == "6":
                from_acc = input("From Account: ")
                to_acc = input("To Account: ")
                amt = float(input("Amount: "))

                src = account_store.find_by_account_number(from_acc)
                dest = account_store.find_by_account_number(to_acc)

                src.withdraw(amt)
                dest.deposit(amt)

                transaction_store.add_transaction(src.get_transactions()[-1])
                transaction_store.add_transaction(dest.get_transactions()[-1])

                print("✅ Transfer completed")

            # ---------------- VIEW ACCOUNTS ---------------- #
            elif choice == "7":
                customer = menu.get_logged_in_customer()
                for acc in customer.get_accounts():
                    print(
                        f"Account: {acc.get_account_number()} | "
                        f"Balance: {acc.get_balance()}"
                    )

            # ---------------- TRANSACTIONS ---------------- #
            elif choice == "8":
                acc_no = input("Account Number: ")
                account = account_store.find_by_account_number(acc_no)

                for tx in menu.show_account_transactions(account):
                    print(
                        f"{tx.get_type()} | "
                        f"{tx.get_amount()} | "
                        f"{tx.get_timestamp()}"
                    )

            # ---------------- LOGOUT ---------------- #
            elif choice == "9":
                menu.logout()
                print("✅ Logged out")

            # ---------------- EXIT ---------------- #
            elif choice == "0":
                print("👋 Thank you for banking with us!")
                break

            else:
                print("❌ Invalid option")

        except Exception as e:
            print(f"⚠ Error: {e}")


if __name__ == "__main__":
    main()