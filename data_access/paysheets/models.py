# -*- coding: utf-8 -*-

from django.db import models
from data_access.base import DomainModel
from data_access.employees.models import Employee, Salary


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None,
                 **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Setting(DomainModel, models.Model):
    basic_salary = models.FloatField()
    transport_assistance = models.FloatField()
    holiday_percentage = models.FloatField()
    unemployment_percentage = models.FloatField()
    unemployment_interest = models.FloatField()
    premium_services = models.FloatField()
    health_percentage = models.FloatField()
    pension_percentage = models.FloatField()
    occupational_hazards = models.FloatField()
    cash_contributions = models.FloatField()
    year = models.PositiveSmallIntegerField()


class Paysheet(DomainModel, models.Model):
    year = models.PositiveSmallIntegerField()
    month = IntegerRangeField(min_value=1, max_value=12)


class PaysheetDetail(DomainModel, models.Model):
    paysheet = models.ForeignKey(Paysheet, on_delete=models.DO_NOTHING)
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    salary = models.ForeignKey(Salary, on_delete=models.DO_NOTHING)
    worked_days = models.PositiveSmallIntegerField()
    basic = models.FloatField()
    transport_assistance = models.FloatField()
    holidays = models.FloatField()
    unemployment = models.FloatField()
    unemployment_interest = models.FloatField()
    premium_services = models.FloatField()
    health = models.FloatField()
    pension = models.FloatField()
    occupational_hazards = models.FloatField()
    cash_contributions = models.FloatField()
    total_accrued = models.FloatField()
    health_percentage = models.FloatField()
    pension_percentage = models.FloatField()
    total_deducted = models.FloatField()
    paid = models.FloatField()



