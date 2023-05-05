from rest_framework import serializers

from books.serializers import BookSerializer
from copies.models import Copy


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Copy
        fields = ["id", "total_book", "period_loan", "book", "users"]
