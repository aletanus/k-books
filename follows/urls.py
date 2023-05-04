from django.urls import path

from copies.views import CopyListCreateView, CopyRetrieveUpdateDestroyAPIView
from follows.views import FollowView, FollowDetailView

urlpatterns = [
    path("follows/", FollowView.as_view(),),
    path("follows/<int:pk>", FollowDetailView.as_view(),),
]
