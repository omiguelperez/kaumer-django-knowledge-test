# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from app.features.paysheets.liquidate_employee import liquidate_employee
from webapps.API.paysheets.requests import LiquidateEmployeeSerializer
from webapps.API.paysheets.responses import LiquidateEmployeeResponse
from webapps.API.base import wrap_exceptions
from drf_yasg.utils import swagger_auto_schema


class PaysheetView(APIView):

    # noinspection PyUnusedLocal
    @swagger_auto_schema(request_body=LiquidateEmployeeSerializer,
                         responses={HTTP_201_CREATED: LiquidateEmployeeResponse})
    @wrap_exceptions
    def post(self, request):
        serializer = LiquidateEmployeeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        output = liquidate_employee(**request.data)
        response = LiquidateEmployeeResponse(output)
        return Response(response.data, status=HTTP_201_CREATED)
