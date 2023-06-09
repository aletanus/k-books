from books.models import Book
from rest_framework import serializers

from books.serializers import BookSerializer
from copies.models import Copy


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        source="book", queryset=Book.objects.all(), write_only=True
    )
    # copy_id = serializers.IntegerField(source="id")

    class Meta:
        model = Copy
        fields = [
            "id",
            "book_total_copies",
            "period_loan",
            "book",
            "book_id",
            "users",
        ]

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.total_book = (
            instance.total_book
            - instance.loans.filter(date_return__isnull=True).count()
        )
        instance.save()
        return instance
