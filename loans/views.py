from rest_framework import generics

from loans.models import Loan
from loans.serializers import LoanSerializer


class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    def perform_create(self, serializer):
        
        return super().perform_create(serializer)

class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
