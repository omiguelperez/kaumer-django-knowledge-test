# -*- coding: utf-8 -*-

from app.features.settings.outputs import SettingOutput
from data_access.paysheets.queries import SettingsQueries
from domain.entities.paysheet import InvalidSetting


def get_current_setting():
    setting = SettingsQueries.get_current_settings()
    if not setting:
        raise InvalidSetting('No hay configuración definida')
    return SettingOutput(setting)
