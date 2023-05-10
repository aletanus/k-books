from django.db import models
from users.models import Users


def book_upload_path(instance, filename):
    return f"books/{instance.id}/{filename}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    launch = models.IntegerField()
    users = models.ManyToManyField(
        Users, through="follows.Follow", related_name="books"
    )

    pdf = models.FileField(upload_to="pdfs", null=True)
    json_data = models.JSONField(null=True)
