from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        calculated_pay = self.hourly_rate * self.hours_worked
        print(f"your payroll is: {calculated_pay}")


class SalaryEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        calculated_pay = self.annual_salary / 12
        print(f"your payroll is: {calculated_pay}")
