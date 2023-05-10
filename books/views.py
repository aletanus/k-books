from rest_framework import generics
from books.models import Book


from books.serializers import BookSerializer
from users.permissions import IsStudentOrCollaboratorViewingStudents

from rest_framework.response import Response
from rest_framework import status


class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]

    def create(self, request, *args, **kwargs):
        pdf_file = request.FILES.get("pdf")
        if pdf_file:
            request.data.pop("pdf")
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        book = serializer.instance
        if pdf_file:
            book.pdf = pdf_file
            book.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsStudentOrCollaboratorViewingStudents]
