from django.db import models

from users.models import Users


class Copy(models.Model):
    total_book = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="copies")
    users = models.ManyToManyField(Users, through="loans.Loan", related_name="copies")
    period_loan = models.IntegerField(default=7)
