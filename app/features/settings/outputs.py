# -*- coding: utf-8 -*-


class SettingOutput:
    def __init__(self, setting):
        self.id = setting.id
        self.basic_salary = setting.basic_salary
        self.transport_assistance = setting.transport_assistance
        self.holiday_percentage = setting.holiday_percentage
        self.unemployment_percentage = setting.unemployment_percentage
        self.unemployment_interest = setting.unemployment_interest
        self.premium_services = setting.premium_services
        self.health_percentage = setting.health_percentage
        self.pension_percentage = setting.pension_percentage
        self.occupational_hazards = setting.occupational_hazards
        self.cash_contributions = setting.cash_contributions
        self.year = setting.year
