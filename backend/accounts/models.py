from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager
# Create your models here.

class User(AbstractBaseUser):
  objects = UserManager()
  userid = models.CharField(max_length=50, unique=True) # minju11012
  phone = models.CharField(max_length=50)
  USERNAME_FIELD = 'userid'
  REQUIRED_FIELDS = []
  def __str__(self):
    return self.userid
