class BankAccount(object):
    # create member variable and set to 0
    balance = 0
    # add parameters to __init__ method

    def __init__(self, name):
        # assign self.name to name param
        self.name = name

    # add __repr__() method
    def __repr__(self):
        # return message stating who account belongs to
        return "This account belongs to %s. Account Balance: %.2f" % (self.name, self.balance)

        # create method that prints just balance
    def show_balance(self):
        print("Balance: %.2f" % self.balance)

        # create method that allows deposits to be made
    def deposit(self, amount):
        # check if amount to deposit is 0 or less
        if amount <= 0:
            print("Insufficient Amount")
            return
        else:
            # print amount added
            print("++ %.2f" % amount)
            # add amount to balance and show updated balance
            self.balance += amount
            self.show_balance()

    def withdraw(self, amount):
        # check if amount to withdraw is larger than balance
        if amount > self.balance:
            print("Insufficient Funds!")
            return
        else:
            # print amount to withdraw
            print("-- %.2f" % amount)
            self.balance -= amount
            self.show_balance()


# create bank account object
my_account = BankAccount("Nasim")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)
