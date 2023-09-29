from django.urls import path
from . import views

urlpatterns = [
    path("dash/", views.UserDashboard.as_view(), name="user-dashboard"),
    path("login/", views.Login.as_view(), name="user-login"),
    path("logout/", views.Logout.as_view(), name='user-logout'),
]
