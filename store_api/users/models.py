from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
  use_in_migrations = True
  def _create_user(self, email, password, **extra_fields):

    if not email:
      raise ValueError('The given username must be set')

    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)
  
  def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
      raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
      raise ValueError('Superuser must have is_superuser=True.')

    return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
  username=None
  email=models.EmailField(_('email address'), unique=True)
  
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

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


class Visitors(models.Model):

  ip = models.CharField(max_length=30, null=True)
  browser = models.CharField(max_length=30)
  location = models.CharField(max_length=100, null=True)
  date_added = models.DateTimeField(default=timezone.now)

  def __str__(self):
    
    self.ip if self.ip else 'N/A'
    self.location if self.location else 'N/A'

    return '{},{} @ {}'.format(self.ip, self.browser, self.location)