from django.urls import path

from copies.views import CopyListCreateView, CopyRetrieveUpdateDestroyAPIView
from loans.views import LoanView, LoanDetailView, LoansByUserView

urlpatterns = [
    path("loans/", LoanView.as_view(),),
    path("loans/<int:pk>", LoanDetailView.as_view(),),
    path("loans/user/<int:user_id>/", LoansByUserView.as_view()),
]
