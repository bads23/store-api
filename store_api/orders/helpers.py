from . import models
from django.db.models import F
from django.utils import timezone
import datetime, json


def ItemsSold():
# Stats for total items sold and pieces per item sold

    queryset = models.OrderItems.objects.select_related('product').all().values('id', 'product', 'product__name', 'quantity', 'buying_price')
    
    items = {}
    objs = []

    for res in queryset:
        id = res['product__name']
        if id not in items:
            items[id] = []
            items[id].append(res)

        else:
            items[id].append(res)

    for key,value in items.items():
        obj = {}
        obj['item'] = key
        obj['quantity'] = 0
        obj['amount'] = 0

        for res in value:
            obj['quantity'] += res['quantity']
            obj['amount'] += res['quantity'] * res['buying_price']


        objs.append(obj)

    return objs


def GatherStats(request):
    # Gathers Statistics aboout orders made
    days = int(request.query_params['days'])
    last_week = timezone.now() - timezone.timedelta(days=days)
    queryset = models.Orders.objects.filter(date_added__range=[last_week, timezone.now()]).order_by('date_added').values('id','name','status','total','date_added')

    items = {}
    objs = []
    
    for x in range(days):
        d = (timezone.now() - timezone.timedelta(days=x))
        d_str = '{0:%d} {0:%b}'.format(d)
        items[d_str] = []

    for res in queryset:
        d = '{0:%d} {0:%b}'.format(res['date_added'])
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
    


    return reversed(objs)
