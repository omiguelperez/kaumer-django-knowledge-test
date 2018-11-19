# -*- coding: utf-8 -*-

from django.urls import path
from webapps.API.paysheets import views

urlpatterns = [
    path('', views.PaysheetView.as_view(), name='paysheet_list'),
    path('<employee_id>/', views.PaysheetDetailView.as_view(), name='paysheet_detail'),
    path('is-liquidated/<employee_id>/', views.verify_liquidated_view,
         name='paysheet_is_liquidated'),
]
