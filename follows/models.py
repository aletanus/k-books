from django.db import models

from books.models import Book
from users.models import Users


class Follow(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
