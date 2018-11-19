# -*- coding: utf-8 -*-

from app.features.paysheets.outputs import EmployeePaysheetDetailOutput
from data_access.paysheets.queries import PaysheetQueries


def get_employee_paysheets(employee_id):
    details = PaysheetQueries.get_by_employee(employee_id)
    output = []
    for detail in details:
        output.append(EmployeePaysheetDetailOutput(detail))
    return output
