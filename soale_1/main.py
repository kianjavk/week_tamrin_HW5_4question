from soale_1 import *


def main():
    while True:
        try:
            name = input("Enter your name: ")
            if not name.isalpha():
                raise ValueError("Name must contain only alphabetic characters")
            if not len(name)>2:
                raise ValueError("Name must be at least 2 characters")
            balance = int(input("Enter your balance: "))

            my_depos = Account(name, balance)

            print(my_depos.__str__())
            print()
            # مقدار تعیین شده
            minimum_balance = 25
            transaction_fee = 0.1

            while True:
                print()
                print('1. To deposit')
                print('2. To withdraw')
                print('3. exit in system')
                choice = input("Choose an option: ").strip()
                if choice in ["1", "2", "3"]:
                    break
                else:
                    print("Invalid choice")

            if choice == '1':
                while True:
                    print('1. To Savings Account')
                    print('2. To checking Account')
                    choice = input("Choose an option: ").strip()
                    if choice in ["1", "2"]:
                        break
                    else:
                        print("Invalid choice")
                        print()
                if choice == '1':
                    amount_deposit = int(input('Enter your deposit amount : '))
                    my_depos.deposit(amount_deposit)
                    print('Deposit Savings Account')
                    print()

                    print("Do you wanna exit system? Yes or No: ")
                    x = input().lower()
                    if x == "yes":
                        print("Have a good day!")
                        break
                elif choice == '2':
                    amount_deposit = int(input('Enter your deposit amount : '))
                    my_depos.deposit(amount_deposit)
                    print('Deposit Checking Account')
                    print()

                    print("Do you wanna exit system? Yes or No: ")
                    x = input().lower()
                    if x == "yes":
                        print("Have a good day!")
                        break


            elif choice == '2':
                while True:
                    print('1. To Savings Account')
                    print('2. To checking Account')
                    choice = input("Choose an option: ").strip()
                    if choice in ["1", "2"]:
                        break
                    else:
                        print("Invalid choice")
                        print()

                if choice == '1':

                    saving = SavingsAccount(my_depos.name, my_depos.balance, minimum_balance)
                    minimum_balance = 25
                    amount_withdraw = int(input('Enter your withdraw amount : '))
                    SavingsAccount(my_depos, amount_withdraw, minimum_balance)
                    saving.withdraw(amount_withdraw)
                    print()

                    print("Do you wanna exit system? Yes or No: ")
                    x = input().lower()
                    if x == "yes":
                        print("Have a good day!")
                        break


                elif choice == '2':

                    checking = CheckingAccount(my_depos.name, my_depos.balance, transaction_fee)
                    transaction_fee = 0.1
                    amount_withdraw = int(input('Enter your withdraw amount : '))
                    print()
                    CheckingAccount(my_depos, amount_withdraw, transaction_fee)
                    checking.withdraw(amount_withdraw)
                    print()

                    print("Do you wanna exit system? Yes or No: ")
                    x = input().lower()
                    if x == "yes":
                        print("Have a good day!")
                        break

            elif choice == '3':
                print('exit in system ...')
                print("Have a good day!")
                break

        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
