from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, UserManager

class CustomUser(AbstractUser):
  email=models.EmailField(_('email address'), unique=True)
  

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
        return self.email


class UserDetails(models.Model):

  phone=models.CharField(max_length=15, null=True)
  city = models.CharField(max_length=30, null=True)
  town = models.CharField(max_length=30, null=True)
  street = models.CharField(max_length=30, null=True)
  house_no = models.CharField(max_length=30, null=True)
  user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

  def __str__(self):
    return self.user