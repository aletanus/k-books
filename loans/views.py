from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.generics import ListAPIView
from copies.models import Copy
from rest_framework.response import Response
from loans.models import Loan
from loans.serializers import LoanSerializer
from users.permissions import IsStudentOrCollaboratorViewingStudents
from django.utils import timezone


class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]

    def create(self, request, *arg, **kwargs):
        copy = get_object_or_404(Copy, pk=request.data["copy_id"])
        if copy.total_book == 0:
            return Response(
                {"error": "This book is not available for loan."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        copy.total_book -= 1
        copy.save()
        serializer = LoanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        if self.request.user.student:
            return Loan.objects.filter(user=self.request.user)
        elif self.request.user.is_superuser:
            return Loan.objects.all()
        else:
            return Loan.objects.none()

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]


class LoansByUserView(ListAPIView):
    serializer_class = LoanSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        if self.request.user.is_superuser or (
            self.request.user.student and user_id == self.request.user.id
        ):
            return Loan.objects.filter(user_id=user_id)
        return Loan.objects.none()


class LoanReturnView(generics.UpdateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.date_return = timezone.now()
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
