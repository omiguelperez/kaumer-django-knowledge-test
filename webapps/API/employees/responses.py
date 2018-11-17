# -*- coding: utf-8 -*-

from rest_framework import serializers


# noinspection PyAbstractClass
class EmployeeResponse(serializers.Serializer):
    id = serializers.UUIDField()
    person_number = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=120)
    last_name = serializers.CharField(max_length=120, allow_blank=True, allow_null=True)
    phone_number = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    salary = serializers.FloatField(required=False)
