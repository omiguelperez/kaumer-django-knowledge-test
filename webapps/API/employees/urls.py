# -*- coding: utf-8 -*-

from django.urls import path
from webapps.API.employees import views

urlpatterns = [
    path('', views.EmployeeView.as_view(), name='employee_list'),
]
