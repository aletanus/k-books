from django.urls import path

from books.views import BookListCreateView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("books/", BookListCreateView.as_view(),),
    path("books/<int:pk>", BookRetrieveUpdateDestroyAPIView.as_view(),),
]
