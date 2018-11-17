# -*- coding: utf-8 -*-

from data_access.employees.queries import EmployeeQueries
from app.features.employees.outputs import EmployeeOutput


def list_employees():
    employees = EmployeeQueries.list()
    output = []
    for employee in employees:
        salary = EmployeeQueries.get_current_salary(employee.id)
        output.append(EmployeeOutput(employee, salary))
    return output
