from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.post_index, name="post-index"),
    path('', views.homepage, name='homepage')
]
