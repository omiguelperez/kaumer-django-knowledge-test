# -*- coding: utf-8 -*-

from rest_framework import serializers


# noinspection PyAbstractClass
class CreateEmployeeSerializer(serializers.Serializer):
    person_number = serializers.CharField(max_length=30)
    name = serializers.CharField(max_length=120)
    last_name = serializers.CharField(max_length=120, allow_null=True, allow_blank=True)
    phone_number = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    salary = serializers.FloatField()
