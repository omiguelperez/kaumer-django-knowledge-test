# -*- coding: utf-8 -*-

from rest_framework import serializers
from webapps.API.employees.responses import EmployeeResponse


# noinspection PyAbstractClass
class PaysheetDetailResponse(serializers.Serializer):
    id = serializers.UUIDField()
    employee = EmployeeResponse()
    salary = serializers.IntegerField()
    worked_days = serializers.IntegerField()
    basic = serializers.FloatField()
    transport_assistance = serializers.FloatField()
    total_accrued = serializers.FloatField()
    health_percentage = serializers.FloatField()
    health = serializers.FloatField()
    pension_percentage = serializers.FloatField()
    pension = serializers.FloatField()
    total_deducted = serializers.FloatField()
    paid = serializers.FloatField()
    holidays = serializers.FloatField()
    unemployment = serializers.FloatField()
    unemployment_interest = serializers.FloatField()
    premium_services = serializers.FloatField()
    occupational_hazards = serializers.FloatField()
    cash_contributions = serializers.FloatField()


# noinspection PyAbstractClass
class LiquidateEmployeeResponse(serializers.Serializer):
    id = serializers.UUIDField()
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    details = PaysheetDetailResponse()


# noinspection PyAbstractClass
class EmployeePaysheetDetailResponse(serializers.Serializer):
    id = serializers.UUIDField()
    salary = serializers.IntegerField()
    worked_days = serializers.IntegerField()
    basic = serializers.FloatField()
    transport_assistance = serializers.FloatField()
    total_accrued = serializers.FloatField()
    health_percentage = serializers.FloatField()
    health = serializers.FloatField()
    pension_percentage = serializers.FloatField()
    pension = serializers.FloatField()
    total_deducted = serializers.FloatField()
    paid = serializers.FloatField()
    holidays = serializers.FloatField()
    unemployment = serializers.FloatField()
    unemployment_interest = serializers.FloatField()
    premium_services = serializers.FloatField()
    occupational_hazards = serializers.FloatField()
    cash_contributions = serializers.FloatField()
    year = serializers.IntegerField()
    month = serializers.IntegerField()
