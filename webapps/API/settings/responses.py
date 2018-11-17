# -*- coding: utf-8 -*-

from rest_framework import serializers


# noinspection PyAbstractClass
class SettingResponse(serializers.Serializer):
    id = serializers.UUIDField()
    basic_salary = serializers.FloatField()
    transport_assistance = serializers.FloatField()
    holiday_percentage = serializers.FloatField()
    unemployment_percentage = serializers.FloatField()
    unemployment_interest = serializers.FloatField()
    premium_services = serializers.FloatField()
    health_percentage = serializers.FloatField()
    pension_percentage = serializers.FloatField()
    occupational_hazards = serializers.FloatField()
    cash_contributions = serializers.FloatField()
    year = serializers.IntegerField()
