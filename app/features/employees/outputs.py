# -*- coding: utf-8 -*-


class EmployeeOutput:
    def __init__(self, employee, salary=None):
        self.id = employee.id
        self.person_number = employee.person_number
        self.name = employee.name
        self.last_name = employee.last_name
        self.email = employee.email
        self.phone_number = employee.phone_number
        if salary:
            self.salary = salary.value
