from books.models import Book
from rest_framework import serializers

from books.serializers import BookSerializer
from copies.models import Copy


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(source="book", queryset=Book.objects.all(), write_only=True)

    class Meta:
        model = Copy
        fields = ["id", "total_book", "period_loan", "book", "book_id", "users"]
