from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Users
from .serializer import UserSerializer

class UserView(CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserDetailview(RetrieveUpdateDestroyAPIView):
    ...