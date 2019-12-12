from . import models
from django.db.models import F
from django.utils import timezone
import datetime, json

def GatherStats(request):
    # Gathers Statistics aboout orders made
    last_week = timezone.now() - timezone.timedelta(days=60)
    queryset = models.Orders.objects.filter(date_added__range=[last_week, timezone.now()]).order_by('date_added').values('id','name','status','total','date_added')

    items = {}
    objs = []

    for res in queryset:
        d = str(res['date_added'].date())
        if d not in items:
            items[d] = []
            res['date_added'] = d
            items[d].append(res)
        else:
            res['date_added'] = d
            items[d].append(res)
    
    for key,value in items.items():
        obj = {}
        obj['date'] = key
        obj['total'] = 0
        obj['orders'] = len(value)

        for res in value:
            obj['total'] += res['total']

        objs.append(obj)
    
    return objs
