from django.urls import path
from . import views

urlpatterns = [
    path("dash/<int:id>", views.UserDashboard.as_view(), name="user-dashboard"),
    path("login/", views.Login.as_view(), name="user-login"),
]
