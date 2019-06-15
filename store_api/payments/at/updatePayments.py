#!/usr/bin/env python

from store_api.payments.models import Payments


def updatePayment(data):
    queryset = Payments.objects.filter(kyc=data['kyc'])

    if(queryset.count() == 1):
        for res in queryset:
            res.status = data['status']
            res.save()
