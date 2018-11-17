# -*- coding: utf-8 -*-

from collections.abc import MutableSequence
from uuid import uuid4


class DetailsCollection(MutableSequence):
    def __init__(self, data=None):
        super(DetailsCollection, self).__init__()
        if data is not None:
            self._list = list(data)
        else:
            self._list = list()

    def __repr__(self):
        return "<{0} {1}>".format(self.__class__.__name__, self._list)

    def __len__(self):
        return len(self._list)

    def __getitem__(self, ii):
        return self._list[ii]

    def __delitem__(self, ii):
        del self._list[ii]

    def __setitem__(self, ii, val):
        self._list[ii] = val

    def __str__(self):
        return str(self._list)

    def insert(self, ii, val):
        self._list.insert(ii, val)

    def append(self, val):
        self.insert(len(self._list), val)


class Paysheet:
    def __init__(self, year, month):
        self.id = uuid4()
        self.year = year
        self.month = month
        self.details = DetailsCollection()

    def liquidate(self, detail):
        self.details.append(detail)

    @staticmethod
    def load(paysheet_id, year, month):
        paysheet = Paysheet(year, month)
        paysheet.id = paysheet_id
        return paysheet


class PaysheetDetail:
    def __init__(self, paysheet, employee, salary, worked_days):
        self.id = uuid4()
        self.paysheet = paysheet
        self.employee = employee
        self.salary = salary
        self.worked_days = worked_days
        self.basic = 0
        self.transport_assistance = 0
        self.total_accrued = 0
        self.health_percentage = 0
        self.health = 0
        self.pension_percentage = 0
        self.pension = 0
        self.total_deducted = 0
        self.paid = 0
        self.holidays = 0
        self.unemployment = 0
        self.unemployment_interest = 0
        self.premium_servicies = 0
        self.occupational_hazards = 0
        self.cash_contributions = 0

    def calculate(self, setting):
        self.basic = self.salary.value * self.worked_days / 30
        self.transport_assistance = self._calculate_transport_assistance(setting)
        self.total_accrued = self.basic + self.transport_assistance
        self.health_percentage = setting.health_percentage
        self.pension_percentage = setting.pension_percentage
        self.health = self.basic * self.health_percentage / 100
        self.pension = self.basic * self.pension_percentage / 100
        self.total_deducted = self.health + self.pension
        self.paid = self.total_accrued - self.total_deducted
        self.holidays = self.salary.value * setting.holiday_percentage / 100
        self.unemployment = self.salary.value * setting.unemployment_percentage / 100
        self.unemployment_interest = self.salary.value * setting.\
            unemployment_interest / 100
        self.premium_servicies = self.salary.value * setting.premium_services / 100
        self.occupational_hazards = self.salary.value * setting.occupational_hazards / 100
        self.cash_contributions = self.salary.value * setting.cash_contributions / 100

    def _calculate_transport_assistance(self, setting):
        if self.salary.value <= setting.transport_assistance * 2:
            return setting.transport_assistance * self.worked_days / 30
        return 0

    @staticmethod
    def load(detail_id, paysheet, employee, salary, worked_days):
        detail = PaysheetDetail(paysheet, employee, salary, worked_days)
        detail.id = detail_id
        return detail


class InvalidSetting(Exception):
    pass


class Setting:
    def __init__(self, basic_salary, transport_assistance, holiday_percentage,
                 unemployment_percentage, unemployment_interest, premium_services,
                 health_percentage, pension_percentage, occupational_hazards,
                 cash_contributions, year):
        self.id = uuid4()
        self.basic_salary = basic_salary
        self.transport_assistance = transport_assistance
        self.holiday_percentage = holiday_percentage
        self.unemployment_percentage = unemployment_percentage
        self.unemployment_interest = unemployment_interest
        self.premium_services = premium_services
        self.health_percentage = health_percentage
        self.pension_percentage = pension_percentage
        self.occupational_hazards = occupational_hazards
        self.cash_contributions = cash_contributions
        self.year = year

    @staticmethod
    def load(setting_id, basic_salary, transport_assistance, holiday_percentage,
             unemployment_percentage, unemployment_interest, premium_services,
             health_percentage, pension_percentage, occupational_hazards,
             cash_contributions, year):
        setting = Setting(basic_salary, transport_assistance, holiday_percentage,
                          unemployment_percentage, unemployment_interest,
                          premium_services, health_percentage, pension_percentage,
                          occupational_hazards, cash_contributions, year)
        setting.id = setting_id
        return setting
