from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.Serializer):
    class Meta:
        model = Book
        fields = "__All__"
