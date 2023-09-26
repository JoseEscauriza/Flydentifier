from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.PostIndex.as_view(), name="post-index"),
    path('', views.Homepage.as_view(), name='homepage'),
    path('about/', views.About.as_view(), name='about'),
]
