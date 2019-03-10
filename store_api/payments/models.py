from django.utils import timezone
from django.db import models


class PaymentModes(models.Model):

  name=models.CharField(max_length=20)
  date_created=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name


class Payments(models.Model):

  name=models.CharField(max_length=20)
  payment_mode=models.ForeignKey(PaymentModes ,on_delete=models.PROTECT)
  amount=models.IntegerField(null=False, blank=False)
  date_created=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name