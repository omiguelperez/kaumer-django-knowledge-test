# -*- coding: utf-8 -*-

from domain.entities.employee import EmployeePersonNumberAlreadyExists
from rest_framework.exceptions import ValidationError
from domain.entities.paysheet import InvalidSetting


def wrap_exceptions(func):
    def func_(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidSetting as exception:
            raise ValidationError(exception)
        except EmployeePersonNumberAlreadyExists as exception:
            raise ValidationError(exception)
    return func_
