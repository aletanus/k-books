from django.urls import path

from copies.views import CopyListCreateView, CopyRetrieveUpdateDestroyAPIView

urlpatterns = [
    path("copies/", CopyListCreateView.as_view(),),
    path("copies/<int:pk>", CopyRetrieveUpdateDestroyAPIView.as_view(),),
]
