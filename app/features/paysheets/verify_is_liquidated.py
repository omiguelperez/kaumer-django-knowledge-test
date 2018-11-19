# -*- coding: utf-8 -*-

from django.utils import timezone
from app.features.paysheets.outputs import VerifyLiquidatedOutput
from data_access.paysheets.queries import PaysheetQueries


def verify_is_liquidated(employee_id):
    now = timezone.now()
    detail = PaysheetQueries.verify(now.year, now.month, employee_id)
    return VerifyLiquidatedOutput(is_liquidated=True if detail else False, detail=detail)
