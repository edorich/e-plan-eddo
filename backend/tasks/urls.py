from django.urls import path
from .views import ProjectsAPIView, AppsAPIView, TasksAPIView

urlpatterns = [
    path('projects/', ProjectsAPIView.as_view(), name="list-create-projects"),
    path('projects/<int:pk>', ProjectsAPIView.as_view(),
         name="detail-update-delete-projects"),
    path('apps/', AppsAPIView.as_view(), name="list-create-apps"),
    path('apps/<int:pk>', AppsAPIView.as_view(),
         name="detail-update-delete-apps"),
    path('', TasksAPIView.as_view(), name="list-create-tasks"),
    path('<int:pk>', TasksAPIView.as_view(),
         name="detail-update-delete-tasks"),
]
