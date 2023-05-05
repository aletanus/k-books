from rest_framework import generics , status
from rest_framework.response import Response 
from follows.models import Follow
from follows.serializers import FollowSerializer
from users.permissions import IsAccountStudent


class FollowView(generics.ListCreateAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAccountStudent]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

       
class FollowDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAccountStudent]

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)
