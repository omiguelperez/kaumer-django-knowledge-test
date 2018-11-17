# -*- coding: utf-8 -*-

from django.utils import timezone
from uuid import uuid4


class EmployeeDoesNotExists(Exception):
    pass


class EmployeeSalaryNotSetted(Exception):
    pass


class EmployeePersonNumberAlreadyExists(Exception):
    pass


class Salary:
    def __init__(self, employee, value):
        self.id = uuid4()
        self.employee = employee
        self.value = value
        self.year = timezone.now().year

    @staticmethod
    def load(salary_id, employee, value, year):
        salary = Salary(employee, value)
        salary.id = salary_id
        salary.year = year
        return salary


class Employee:
    def __init__(self, person_number, name, last_name, email, phone_number):
        self.id = uuid4()
        self.person_number = person_number
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def load(employee_id, person_number, name, last_name, email, phone_number):
        emp = Employee(person_number, name, last_name, email, phone_number)
        emp.id = employee_id
        return emp
