# -*- coding: utf-8 -*-

from rest_framework import serializers


# noinspection PyAbstractClass
class LiquidateEmployeeSerializer(serializers.Serializer):
    employee_id = serializers.UUIDField()
    worked_days = serializers.IntegerField()
