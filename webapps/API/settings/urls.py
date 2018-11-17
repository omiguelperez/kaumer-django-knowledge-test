# -*- coding: utf-8 -*-

from django.urls import path
from webapps.API.settings import views

urlpatterns = [
    path('', views.SettingView.as_view(), name='setting_list'),
]
