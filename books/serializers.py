from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "author", "launch", "users", "pdf"]
        extra_kwargs = {"json_data": {"write_only": True}}
