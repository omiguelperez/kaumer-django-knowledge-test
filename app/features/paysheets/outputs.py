# -*- coding: utf-8 -*-

from app.features.employees.outputs import EmployeeOutput


class PaysheetDetailOutput:
    def __init__(self, detail):
        self.id = detail.id
        self.employee = EmployeeOutput(detail.employee)
        self.salary = detail.salary.value
        self.worked_days = detail.worked_days
        self.basic = detail.basic
        self.transport_assistance = detail.transport_assistance
        self.total_accrued = detail.total_accrued
        self.health_percentage = detail.health_percentage
        self.health = detail.health
        self.pension_percentage = detail.pension_percentage
        self.pension = detail.pension
        self.total_deducted = detail.total_deducted
        self.paid = detail.paid
        self.holidays = detail.holidays
        self.unemployment = detail.unemployment
        self.unemployment_interest = detail.unemployment_interest
        self.premium_services = detail.premium_services
        self.occupational_hazards = detail.occupational_hazards
        self.cash_contributions = detail.cash_contributions


class PaysheetOutput:
    def __init__(self, paysheet, details):
        self.id = paysheet.id
        self.year = paysheet.year
        self.month = paysheet.month
        self.details = [PaysheetDetailOutput(detail) for detail in details]
