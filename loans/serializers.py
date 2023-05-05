from rest_framework import serializers

from copies.serializers import CopySerializer
from loans.models import Loan
from users.serializer import UserSerializer


class LoanSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    copy = CopySerializer()

    class Meta:
        model = Loan
        fields = ["id", "date_loan", "date_return", "user", "copy"]
