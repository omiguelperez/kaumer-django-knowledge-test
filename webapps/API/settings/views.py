# -*- coding: utf-8 -*-

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED
from app.features.settings.get_current_setting import get_current_setting
from webapps.API.settings.responses import SettingResponse
from webapps.API.base import wrap_exceptions
from drf_yasg.utils import swagger_auto_schema


class SettingView(APIView):

    # noinspection PyUnusedLocal
    @swagger_auto_schema(responses={HTTP_200_OK: SettingResponse})
    @wrap_exceptions
    def get(self, request):
        output = get_current_setting()
        response = SettingResponse(output)
        return Response(response.data, status=HTTP_200_OK)
