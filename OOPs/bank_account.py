from abc import ABCMeta

class Account:
    __metaclass__ = ABCMeta

    def check_balance(self):
        return self.balance

    def deposit(self, bal):
        self.balance += bal

    def withdraw(self, bal):
        self.balance-= bal

class Checking(Account):

    def __init__(self):
        self.balance = 0

class Savings(Account):

    def __init__(self):
        self.balance = 0

class Buisness(Account):

    def __init__(self):
        self.balance = 0


check = Checking()
save = Savings()
biz = Buisness()

done = False

def get_account(x):
    if x < 1 or x > 3:
        print "invalid input \n Aborting . .. . . .. . . "
        raise IndexError

    accnts = {1 : check, 2 : save, 3 : biz}
    return accnts[x]

def action(acc, x):
    if x < 1 or x > 3:
        print "invalid input \n Aborting . .. . . .. . . "
        raise IndexError

    if x == 1:
        return acc.check_balance()
    elif x == 2:
        bal = float(raw_input("Enter the amount: "))
        acc.withdraw(bal)
        return acc.check_balance()
    elif x == 3:
        bal = float(raw_input("Enter the amount: "))
        acc.deposit(bal)
        return acc.check_balance()


while not done:
    acc = get_account(int(raw_input("What type of account: \n 1. Checking \n 2. Savings \n 3. Buisness \n")))
    new_bal = action(acc, int(raw_input("What do you want: \n 1. Check Balance \n 2. Withdrawal \n 3. Deposit \n")))
    print ("New Balance: {0}").format(new_bal)

    if int(raw_input("Done: \n 1. Yes \n 2. No \n")) == 1:
        done = True
