from . import models
from django.db.models import F
from django.utils import timezone
import datetime, json

def VisitorStats():

    queryset = models.Visitors.objects.all()

    items = {}
    objs = []
    for res in queryset:
        u = res.ip

        if u not in items:
            items[u] = []
            items[u].append(res)
        else:
            items[u].append(res)
    
    for key,value in items.items():
        obj = {}
        obj['ip'] = key
        obj['visits'] = len(value)

        objs.append(obj)

    return objs