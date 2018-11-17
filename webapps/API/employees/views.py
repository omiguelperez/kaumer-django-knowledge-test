# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from app.features.employees.create_employee import create_employee
from app.features.employees.list_employees import list_employees
from webapps.API.employees.requests import CreateEmployeeSerializer
from webapps.API.employees.responses import EmployeeResponse
from webapps.API.base import wrap_exceptions
from drf_yasg.utils import swagger_auto_schema


class EmployeeView(APIView):

    # noinspection PyUnusedLocal
    @swagger_auto_schema(request_body=CreateEmployeeSerializer,
                         responses={HTTP_201_CREATED: EmployeeResponse})
    @wrap_exceptions
    def post(self, request):
        serializer = CreateEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        output = create_employee(**serializer.data)
        response = EmployeeResponse(output)
        return Response(response.data, status=HTTP_201_CREATED)

    # noinspection PyUnusedLocal
    @swagger_auto_schema(responses={HTTP_200_OK: EmployeeResponse(many=True)})
    @wrap_exceptions
    def get(self, request):
        output = list_employees()
        response = EmployeeResponse(output, many=True)
        return Response(response.data, status=HTTP_200_OK)
