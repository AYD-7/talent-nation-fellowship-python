# Banking System
# Bank Account
class BankAccount :
    # initialization
    def __init__(self, name, number, balance):
        self.name = name
        self.number = number
        # encapsulation
        self.__balance = balance

    # check balance
    def check_balance (self):
        print(f"self.__balance")