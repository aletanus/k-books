from django.db import models

from users.models import Users


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    launch = models.IntegerField()
    users = models.ManyToManyField(Users, through="follows.Follow", related_name="books")
