from django.urls import path
from .views import SignupView, UserAccountListAPIView

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('', UserAccountListAPIView.as_view(), name="list-accounts"),
    path('<int:pk>', UserAccountListAPIView.as_view(),
         name="detail-update-delete-accounts"),
]
