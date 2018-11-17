# -*- coding: utf-8 -*-

from domain.entities.employee import Employee, Salary
from data_access.employees.models import Employee as EmployeeORM, Salary as SalaryORM


class EmployeeQueries:

    @staticmethod
    def add(employee):
        EmployeeORM.objects.create(id=employee.id, name=employee.name,
                                   person_number=employee.person_number,
                                   last_name=employee.last_name, email=employee.email,
                                   phone_number=employee.phone_number)

    @staticmethod
    def set_salary(salary):
        SalaryORM.objects.create(id=salary.id, employee_id=salary.employee.id,
                                 value=salary.value, year=salary.year)

    @staticmethod
    def get(employee_id):
        employee = EmployeeORM.objects.filter(pk=employee_id).first()
        return Employee.load(employee.id, employee.person_number, employee.name,
                             employee.last_name, employee.email, employee.phone_number)\
            if employee else None

    @staticmethod
    def get_current_salary(employee_id):
        salary = SalaryORM.objects.filter(employee_id=employee_id).last()
        return Salary.load(salary.id, salary.employee, salary.value, salary.year) if \
            salary else None

    @staticmethod
    def list():
        items = EmployeeORM.objects.all()
        employees = []
        for item in items:
            employees.append(Employee.load(item.id, item.person_number, item.name,
                                           item.last_name, item.email,
                                           item.person_number))
        return employees
