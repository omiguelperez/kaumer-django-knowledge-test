# -*- coding: utf-8 -*-

from domain.entities.employee import Employee, Salary
from data_access.employees.queries import EmployeeQueries
from app.features.employees.outputs import EmployeeOutput


def create_employee(person_number, name, last_name, email, phone_number, salary):
    employee = Employee(person_number, name, last_name, email, phone_number)
    salary = Salary(employee, salary)
    EmployeeQueries.add(employee)
    EmployeeQueries.set_salary(salary)
    return EmployeeOutput(employee, salary=salary)
