# -*- coding: utf-8 -*-

from data_access.paysheets.models import Paysheet as PaysheetORM, PaysheetDetail as \
    PaysheetDetailORM, Setting as SettingsORM
from domain.entities.paysheet import Paysheet, Setting


class PaysheetQueries:

    @staticmethod
    def add(paysheet):
        PaysheetORM.objects.create(id=paysheet.id, year=paysheet.year,
                                   month=paysheet.month)

    @staticmethod
    def get_by_date(year, month):
        paysheet = PaysheetORM.objects.filter(year=year, month=month).first()
        return Paysheet.load(paysheet.id, paysheet.year, paysheet.month) if paysheet \
            else None

    @staticmethod
    def update(paysheet, detail):
        PaysheetDetailORM.objects.create(id=detail.id, paysheet=paysheet.id,
                                         employee=detail.employee.id,
                                         salary=detail.salary.id,
                                         worked_days=detail.worked_days,
                                         basic=detail.basic,
                                         transport_assistance=detail.transport_assistance,
                                         total_accrued=detail.total_accrued,
                                         health_percentage=detail.health_percentage,
                                         pension_percentage=detail.pension_percentage,
                                         healt=detail.healt, pension=detail.pension,
                                         total_deducted=detail.total_deducted,
                                         paid=detail.paid)

    @staticmethod
    def get_by_employee(employee_id):
        pass


class SettingsQueries:

    @staticmethod
    def add(setting):
        SettingsORM.\
            objects\
            .create(id=setting.id, basic_salary=setting.basic_salary,
                    transport_assistance=setting.transport_assistance,
                    holiday_percentage=setting.holiday_percentage,
                    unemployment_percentage=setting.unemployment_percentage,
                    unemployment_interest=setting.unemployment_interest,
                    premium_services=setting.premium_services,
                    health_percentage=setting.health_percentage,
                    pension_percentage=setting.pension_percentage,
                    occupational_hazards=setting.occupational_hazards,
                    cash_contributions=setting.cash_contributions, year=setting.year)

    @staticmethod
    def _render_setting(setting):
        return Setting.load(setting.id, setting.basic_salary,
                            setting.transport_assistance, setting.holiday_percentage,
                            setting.unemployment_percentage,
                            setting.unemployment_interest, setting.premium_services,
                            setting.health_percentage, setting.pension_percentage,
                            setting.occupational_hazards, setting.cash_contributions,
                            setting.year) if setting else None

    @staticmethod
    def get_by_year(year):
        setting = SettingsORM.objects.filter(year=year).first()
        return SettingsQueries._render_setting(setting)

    @staticmethod
    def get_current_settings():
        setting = SettingsORM.objects.last()
        return SettingsQueries._render_setting(setting)
