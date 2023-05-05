from rest_framework import serializers

from books.models import Book
from books.serializers import BookSerializer
from follows.models import Follow
from users.serializer import UserSerializer


class FollowSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(source="book", queryset=Book.objects.all(), write_only=True)

    class Meta:
        model = Follow
        fields = "__all__"
