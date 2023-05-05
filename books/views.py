from rest_framework import generics

from books.models import Book
from books.serializers import BookSerializer
from users.permissions import IsStudentOrCollaboratorViewingStudents


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]

