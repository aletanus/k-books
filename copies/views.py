from rest_framework import generics

from copies.models import Copy
from copies.serializers import CopySerializer


class CopyListCreateView(generics.ListCreateAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer


class CopyRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Copy.objects.all()
    serializer_class = CopySerializer
