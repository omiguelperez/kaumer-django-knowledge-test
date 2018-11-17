# -*- coding: utf-8 -*-

from django.utils import timezone
from app.features.settings.outputs import SettingOutput
from data_access.paysheets.queries import SettingsQueries
from domain.entities.paysheet import Setting


def save_setting(basic_salary, transport_assistance, holiday_percentage,
                 unemployment_percentage, unemployment_interest, premium_services,
                 health_percentage, pension_percentage, occupational_hazards,
                 cash_contributions):
    year = timezone.now().year
    setting = SettingsQueries.get_by_year(year)
    if not setting:
        setting = Setting(basic_salary, transport_assistance, holiday_percentage,
                          unemployment_percentage, unemployment_interest, premium_services,
                          health_percentage, pension_percentage, occupational_hazards,
                          cash_contributions, year)
        SettingsQueries.add(setting)
    return SettingOutput(setting)
