# -*- coding: utf-8 -*-

from rest_framework import serializers


# noinspection PyAbstractClass
class LiquidateEmployeeSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    employee_id = serializers.UUIDField()
    worked_days = serializers.CharField(max_length=25)
