# -*- coding: utf-8 -*-

from django.urls import path, include

urlpatterns = [
    path('employees/', include('webapps.API.employees.urls')),
    path('paysheets/', include('webapps.API.paysheets.urls')),
    path('settings/', include('webapps.API.settings.urls')),
]
