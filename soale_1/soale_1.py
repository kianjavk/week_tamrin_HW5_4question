class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'Account name :{self.name}, Account amount {self.balance}'

    def withdraw(self, amount_withdraw):
        if amount_withdraw < self.balance:
            self.balance -= amount_withdraw
            print(f'balance :{self.balance}')

        else:
            print('You cannot withdraw more than your balance')

    def deposit(self, amount_deposit):
        if amount_deposit > 0:
            self.balance += amount_deposit
            print(f'balance :{self.balance}')
            return f'deposit amount :{amount_deposit}'
        else:
            print('deposit amount cant be ziro')


class SavingsAccount(Account):
    def __init__(self, name, balance, minimum_balance):
        super().__init__(name, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount_withdraw):
        if amount_withdraw < self.balance:
            if self.balance - amount_withdraw < self.minimum_balance:

                print("can't withdraw if balance gets less than minimum balance")
            else:
                self.balance -= amount_withdraw
                print(f'balance :{self.balance}, minimum balance :{self.minimum_balance}')
        else:
            print('You cannot withdraw more than your balance')


class CheckingAccount(Account):
    def __init__(self, name, balance, transaction_fee):
        super().__init__(name, balance)
        self.transaction_fee = transaction_fee

    def withdraw(self, amount_withdraw):
        fee = amount_withdraw * self.transaction_fee
        new_balance = self.balance - (amount_withdraw + fee)
        if new_balance <= 0:
            print('You cannot withdraw more than your balance')
        else:
            print(
                f'new balance :{new_balance}, amount withdraw {amount_withdraw}, transaction fee {self.transaction_fee}')


