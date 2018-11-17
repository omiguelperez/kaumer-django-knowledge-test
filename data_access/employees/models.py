# -*- coding: utf-8 -*-

from django.db import models
from data_access.base import DomainModel


class Employee(DomainModel, models.Model):
    person_number = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120, blank=True, null=True)
    phone_number = models.CharField(max_length=25)
    email = models.EmailField(max_length=50)


class Salary(DomainModel, models.Model):
    value = models.FloatField()
    year = models.PositiveSmallIntegerField()
    employee = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
