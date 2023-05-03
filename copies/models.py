from django.db import models


class Copy(models.Model):
    total_book = models.IntegerField()
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="copies")
