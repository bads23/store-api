from django.utils import timezone
from django.db import models
import string,random
from  datetime import datetime

def generateOrderName(user_id):
    randomstr = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    now = datetime.now().strftime("%d%m%y")
    new_name = '{}-{}-{}'.format(user_id, randomstr, now)
    return new_name

class PaymentModes(models.Model):

  name=models.CharField(max_length=20)
  date_created=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name


class Payments(models.Model):

  name=models.CharField(max_length=20)
  payment_mode=models.ForeignKey(PaymentModes ,on_delete=models.PROTECT)
  phone_number=models.CharField(max_length=20, null=True)
  amount=models.IntegerField(null=False, blank=False)
  status=models.CharField(max_length=50, null=True)
  transactionId=models.CharField(max_length=50, null=True)
  date_created=models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.name
  
  def save(self, *args, **kwargs):
    if(self.name == ''):
      self.name = generateOrderName(self.pk)
    super(Payments, self).save(*args, **kwargs)