# -*- coding: utf-8 -*-

from django.utils import timezone
from app.features.paysheets.outputs import PaysheetOutput
from data_access.employees.queries import EmployeeQueries
from data_access.paysheets.queries import PaysheetQueries, SettingsQueries
from domain.entities.employee import EmployeeDoesNotExists, EmployeeSalaryNotSetted
from domain.entities.paysheet import Paysheet, PaysheetDetail, InvalidSetting


def liquidate_employee(employee_id, worked_days):
    now = timezone.now()
    year = now.year
    month = now.month

    paysheet = PaysheetQueries.get_by_date(year, month)
    if not paysheet:
        paysheet = Paysheet(year, month)
        PaysheetQueries.add(paysheet)

    employee = EmployeeQueries.get(employee_id)
    if not employee:
        raise EmployeeDoesNotExists('El empleado %s no existe' % employee_id)

    salary = EmployeeQueries.get_current_salary(employee.id)
    if not salary:
        raise EmployeeSalaryNotSetted('El empleado %s no tiene un salario definido' %
                                      employee.id)

    setting = SettingsQueries.get_current_settings()
    if not setting:
        raise InvalidSetting('No se ha configurado el sistema')

    detail = PaysheetDetail(paysheet, employee, salary, worked_days)
    detail.calculate(setting)

    PaysheetQueries.update(paysheet, detail)

    return PaysheetOutput(paysheet, [detail])
