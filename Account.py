class Account:
    def __init__(self,number,pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.owner = "new_person"
        self.limit = 0
        self.__interest_rate = 0.05
        self. freeze = True
        self.min_balance = 0
        self.__transfer_fee =0
    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance
        else:
            return "Wrong pin"
    # Method to display the account owner's details and current balance.
    def show_details(self, pin):
        if pin == self.__pin:
            return self.number and self.__balance
        else:
            return "Wrong Pin"
    # Method to update the account owner's information.
    def update_owner_information(self,owner):
        self.owner = owner
    #  Method to generate a statement of recent transactions.
    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount
            self.__transactions.append(("Deposit", amount))
            return f" You have Deposited {amount} successfully."
        else:
            return "Wrong pin"
    def withdraw(self, amount, pin):
        if pin == self.__pin and self.__balance >= amount:
            self.__balance -= amount
            self.__transactions.append(("Withdrawal", amount))
            return f"You Withdrew {amount} successfully."
        else:
            return "Insufficient funds top up."
    def generate_statement(self, pin):
        if pin == self.__pin:
            statement = "Recent Transactions:\n"
            return statement
        else:
            return "Wrong pin"
        # Method to set an overdraft limit for the account.
    def set_overdraft_limit(self, limit, pin):
        if pin == self.__pin:
            self.limit = limit
            return f"Your're overdraft limit set to {limit}."
        else:
          return " You entered the Wrong pin"
        # Method to calculate and apply interest to the balance.
    def apply_interest(self, pin):
        if pin == self.__pin:
            interest = self.__balance * self.__interest_rate
            self.__balance += interest
            self.__transactions.append(("Interest", interest))
            return f"An interest of {interest} was applied successfully."
        else:
          return "Wrong pin"
        # Methods to freeze and unfreeze the account for security reasons.
    def freezing_account(self, pin):
        if pin == self.__pin:
            self.freeze = True
            return "Your account was flozen successfully."
        else:
          return "Wrong pin"
    def unfreeze_account(self, pin):
        if pin == self.__pin:
            self.freeze = False
            return "unfreeze  account successfully."
        else:
          return "Wrong pin"
        #Retrieve the history of all transactions made on the account.
    def get_history(self, pin):
        if pin == self.__pin:
            history = "Transaction History:\n"
            return history
        else:
           return "Wrong pin"
    #    Method to enforce a minimum balance requirement.
    def set_minimum_balance(self, minimum_balance, pin):
        if pin == self.__pin:
            self.mininimum_balance = minimum_balance
            return f"Minimum balance set to {minimum_balance}."
        else:
          return "Wrong pin"
    #    Method to transfer funds from one account to another.
    def transfer_funds(self, amount, account):
        if self.__balance >= amount + self.__transfer_fee and not self.freeze:
            self.__balance = amount + self.__transfer_fee
            account.deposit(amount, account.__pin)
            return f"Transferred {amount} to {account} successfully."
        else:
          return "Unable to process transfer."
    #   Method to close the account and perform necessary cleanup.
    def close_account(self, pin):
        if pin == self.__pin and self.__balance == 0:
            self.freeze = True
            return "Account closed successfully."
        else:
          return "Unable to close account."