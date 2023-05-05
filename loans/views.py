from rest_framework import generics, status
from rest_framework.response import Response
from loans.models import Loan
from loans.serializers import LoanSerializer
from copies.models import Copy
from django.shortcuts import get_object_or_404
class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    
    
class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer






























    def create(self, request, *arg, **kwargs):
        copy = get_object_or_404(Copy, pk=request.data['copy'])
        if copy.total_book == 0:
            return Response({'error': 'This book is not available for loan.'}, status=status.HTTP_400_BAD_REQUEST)
        copy.total_book -= 1
        copy.save()
        serializer = LoanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)