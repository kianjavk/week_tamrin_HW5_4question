from soale_2 import *


def main():
    while True:
        try:
            e_list=[]
            e_name = input("enter employee name: ")
            if not e_name.isalpha():
                raise ValueError
            # for i in e_name:

            with open('employees.txt', 'a') as file:
                file.write(str(f'employee name : {e_name}'))
                file.write('\n')

            while True:
                print("1. hourly employee: ")
                print("2. salary employee: ")
                print("3. exit in system: ")
                print()
                choice = input("Choose an option: ").strip()
                if choice in ["1", "2", "3"]:
                    break
                else:
                    print("Invalid choice")
            if choice == "1":
                hourly_rate = float(input("enter hourly rate value: "))
                hours_worked = float(input("enter hours worked value: "))
                hourly_obj = HourlyEmployee(e_name, hourly_rate, hours_worked)
                print()
                print(f"employee {e_name} has been paid {hourly_obj.calculate_pay()}")
                print()

                print("Do you wanna exit system? Yes or No: ")
                x = input().lower()
                if x == "yes":
                    print("Have a nice day!")
                    break

            elif choice == "2":
                annual_salary = float(input("enter annual salary value: "))
                salary_obj = SalaryEmployee(e_name, annual_salary)
                print()
                print(f"employee {e_name} has been paid {salary_obj.calculate_pay()}")
                print()

                print("Do you wanna exit system? Yes or No: ")
                x = input().lower()
                if x == "yes":
                    print("Have a nice day!")
                    break

            elif choice == "3":
                print("exit in system.")
                print("Have a nice day!")
                break
        except ValueError as e:
            print(f"Invalid input {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
