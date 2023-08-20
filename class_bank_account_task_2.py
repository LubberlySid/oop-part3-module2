"""
   In this program we see a representation of our bank account
                                                              """


class BankAccount:
    """
       This class is created for represent our bank account
                                                           """

    def __init__(self, balance, amount_of_money, depo, account_number):
        """
           In this function we created variables which means we use in our functions
                                                                                    """
        self.amount_of_money = amount_of_money
        self.balance = balance
        self.account_number = account_number
        self.depo = depo

    def withdraw(self):
        """
           In this function we check if amount of money to withdraw is allowable
                                                                                """
        if 0 < self.amount_of_money < self.balance:
            self.balance -= self.amount_of_money
            return True

        return None

    def deposit(self):
        """
           In this function we deposit money on our bank account
                                                                """
        if self.depo > 0:
            self.balance += self.depo
            return True

        return None

    def __str__(self):
        """
           In this function we output the result of our program
                                                               """
        return f"Account Number: {self.account_number}. Balance: {self.balance}$"


account = BankAccount(1000, 500, 55, "132457689")
print(account)

account.withdraw()
print(account)
account.deposit()
print(account)
