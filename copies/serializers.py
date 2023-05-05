from rest_framework import serializers

from books.serializers import BookSerializer
from copies.models import Copy


class CopySerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Copy
        fields = ["id", "total_book", "period_loan", "book", "users"]
        
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.total_book = instance.total_book - instance.loans.filter(date_return__isnull=True).count()
        instance.save()
        return instance
