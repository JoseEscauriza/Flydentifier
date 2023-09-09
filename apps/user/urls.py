from django.urls import path
from . import views

urlpatterns = [
    path("dash/<int:id>", views.user_dashboard, name="user-dashboard"),
]
