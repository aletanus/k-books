from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=122)
    student = models.BooleanField(default=False)
    blocked = models.BooleanField(default=False)
 