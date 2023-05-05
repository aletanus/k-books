from rest_framework import generics
from rest_framework.generics import ListAPIView

from loans.models import Loan
from loans.serializers import LoanSerializer
from users.permissions import IsStudentOrCollaboratorViewingStudents


class LoanView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]

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
        if self.request.user.is_superuser or (self.request.user.student and user_id == self.request.user.id):
            return Loan.objects.filter(user_id=user_id)
        return Loan.objects.none()
