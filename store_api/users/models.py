from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.hashers import make_password
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser


class CustomUserManager(BaseUserManager):

  def create_user(self, email, first_name, last_name, date_created, password=None, is_staff=False, **extra_fields):

    now = timezone.now()
    validate_email(email)
    p = make_password(password)

    user = self.model(
      email= self.normalize_email(email),
      first_name= first_name,
      last_name= last_name,
      password= p,
      is_staff= is_staff,
      date_created = now,
    )

    user.is_active = True
    user.save(using=self._db)
    return user

  def create_superuser(self, email, first_name, last_name, date_created, password=None, is_staff=True, **extra_fields):

    user = self.create_user(
      email, first_name, last_name, password, date_created, **extra_fields
    )
    user.is_staff = is_staff
    user.save(using=self._db)
    return user

class CustomUser(AbstractBaseUser):

  email=models.EmailField(unique=True)
  first_name=models.CharField(max_length=30)
  last_name=models.CharField(max_length=30, blank=True)
  date_created=models.DateTimeField(default=timezone.now)
  is_staff=models.BooleanField(default=False)
  is_active=models.BooleanField(default=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  objects = CustomUserManager()

  class Meta:
    verbose_name = _('user')
    verbose_name_plural = _('users')

  def get_full_name(self):
    full_name = '{} {}'.format(self.first_name, self.last_name)
    return full_name

  def get_short_name(self):
    return self.first_name

  def save(self, *args, **kwargs):
    super(CustomUser, self).save(*args, **kwargs)