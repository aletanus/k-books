from rest_framework import serializers

from copies.models import Copy
from copies.serializers import CopySerializer
from loans.models import Loan
from users.models import Users
from users.serializer import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    copy = CopySerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(source="user", queryset=Users.objects.all(), write_only=True)
    copy_id = serializers.PrimaryKeyRelatedField(source="copy", queryset=Copy.objects.all(), write_only=True)

    class Meta:
        model = Loan
        fields = "__all__"
