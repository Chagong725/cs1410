import os
from abc import ABC, abstractmethod
import csv

EMPLOYEE_FILE = 'employees.csv'
PAY_LOGFILE = 'paylog.txt'
RECEIPT_FILE = 'receipts.csv'

employees = []


class Employee:
    def __init__(self, emp_id, first_name, last_name, address, city, state, zipcode, classification):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = classification


class Classification(ABC):
    @abstractmethod
    def compute_pay(self):
        return 0


class Hourly(Classification, ABC):
    def __init__(self, hourly_rate, hours_worked=None, time_cards=None):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.time_cards = time_cards or []

    def compute_pay(self):
        total_pay = sum(self.time_cards) * float(self.hourly_rate)
        return total_pay

    def process_timecard(self, hours):
        self.time_cards.append(hours)


class Salary(Classification, ABC):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        return self.salary


class Commissioned(Classification, ABC):
    def __init__(self, salary, commission_rate, *args):
        self.salary = salary
        self.commission_rate = commission_rate
        self.sales = list(args)

    def compute_pay(self):
        total_sales = sum(self.sales)
        commission_pay = total_sales * float(self.commission_rate)
        total_pay = commission_pay + float(self.salary)
        return total_pay

    def add_receipt(self, amount):
        self.sales.append(amount)


def load_employees(hours_worked, employee_sales_dict):
    paylog = []
    with open('employees.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # ignores the first line
        for row in reader:
            emp_id, first_name, last_name, address, city, state, zipcode, classification, *classification_args = row
            if classification == "3":
                hourly_rate = classification_args[2]
                employee_classification = Hourly(float(hourly_rate))
                total_pay = float(hourly_rate) * hours_worked[emp_id]
            elif classification == "1":
                salary = classification_args[0]
                employee_classification = Salary(float(salary))
                total_pay = float(salary) / 24
            elif classification == "2":
                commission_rate = float(classification_args[1])/100
                salary = classification_args[0]
                employee_classification = Commissioned(float(commission_rate), float(salary))
                if emp_id in employee_sales_dict:
                    commission = employee_sales_dict[emp_id] * float(commission_rate)
                else:
                    commission = 0.0
                total_pay = commission + float(salary) / 24
            else:
                raise ValueError(f"Unknown Classification: {classification}")
            employee = Employee(emp_id, first_name, last_name, address, city, state, zipcode, employee_classification)
            employees.append(employee)
            paylog.append(f"Mailing {round(total_pay, 2)} to {employee.first_name} {employee.last_name} at "
                          f"{employee.address} {employee.city} {employee.state} {employee.zipcode}\n")
    for paylog_string in paylog:
        print(paylog_string)
    return paylog


def find_employee_by_id(employee_id):
    for emp in employees:
        if emp.emp_id == employee_id:
            return emp


def process_timecards():
    with open('timecards.csv', 'r') as file:
        hours_worked = {}
        for line in file:
            employee_card = line.split(",")
            emp_id = employee_card[0]
            hours = [float(hour) for hour in employee_card[1:]]
            if emp_id in hours_worked:
                hours_worked[emp_id] += sum(hours)
            else:
                hours_worked[emp_id] = sum(hours)

        with open('employees.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # ignores the first line
            for row in reader:
                emp_id = row[0]
                if emp_id not in hours_worked:
                    hours_worked[emp_id] = 0
    return hours_worked


def process_receipts():
    employee_sales_dict = {}
    new_employee_sales = {}
    with open('receipts.csv', 'r') as file:
        for line in file:
            employee_sales = line.split(",")
            employee_id = employee_sales[0]
            sales_data = employee_sales[1:]

            total_sales = sum(float(sale) for sale in sales_data)

            if employee_id in employee_sales_dict:
                employee_sales_dict[employee_id] += total_sales
            else:
                employee_sales_dict[employee_id] = total_sales

        with open('receipts.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)  # ignores the first line
            for row in reader:
                emp_id = row[0]
                if emp_id not in employee_sales_dict:
                    new_employee_sales[emp_id] = 0

    employee_sales_dict.update(new_employee_sales)
    return employee_sales_dict


def run_payroll():
    if os.path.exists(PAY_LOGFILE):  # pay_log_file is a global variable holding ‘paylog.txt’
        os.rename(PAY_LOGFILE, "paylog_old.txt")
    hours_worked = process_timecards()
    employee_sales_dict = process_receipts()
    paylog_text = load_employees(hours_worked, employee_sales_dict)
    paylog_file = open(PAY_LOGFILE, "w")
    for paylog_line in paylog_text:
        paylog_file.write(paylog_line)
    paylog_file.close()


if __name__ == "__main__":
    run_payroll()
